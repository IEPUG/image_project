from flask import Flask
from flask.ext import restful
import queryImages

app = Flask(__name__)
api = restful.Api(app)


@app.route("/")
def hello():
    return "Hello from plain old flask"


class APIRoot(restful.Resource):
    def get(self):
        return {'context': 'api',
                'message': 'Hello, World!'}

api.add_resource(APIRoot, '/api/v1/')


class APIImages(restful.Resource):
    def __init__(self):
        self.imageReader = queryImages.ImageReader()

    def get(self):
        self.imageReader.query()
        results = []
        for i, result in enumerate(self.imageReader.results):
            resultDict = {
                "id": result.id,
                "longitude": result.longitude,
                "latitude": result.latitude
            }
            results.append(resultDict)
        return {'images': results}

api.add_resource(APIImages, '/api/v1/images/')

if __name__ == "__main__":
    app.run()
