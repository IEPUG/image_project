from flask import Flask
from flask.ext import restful


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
    def get(self):
        return {'images': {}}

api.add_resource(APIImages, '/api/v1/images/')

if __name__ == "__main__":
    app.run()
