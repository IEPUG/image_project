from flask import Flask
from flask_restful import reqparse, Api, Resource
from flask.json import JSONEncoder
import queryImages

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello():
    return "Hello from plain old flask"

class APIRoot(Resource):
    def get(self):
        return {'context': 'api',
                'message': 'Hello, World!'}

api.add_resource(APIRoot, '/api/v1/')

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=True,
                    help="ID can not be blank!")


class APIImages(Resource):
    def __init__(self):
        self.imageReader = queryImages.ImageReader()

    def get(self):
        self.imageReader.queryAll()
        results = []
        for i, result in enumerate(self.imageReader.results):
            resultDict = {
                "id": result.id,
                "longitude": result.longitude,
                "latitude": result.latitude
            }
            results.append(resultDict)
        return {'images': results}

    def post(self):
        args = parser.parse_args()
        self.imageReader.queryById(args["id"])
        result = self.imageReader.imageInfo
        resultDict = {
            "sourceUrl": result.sourceUrl,
            "dateRetreived": str(result.dateRetreived),
            "imageDate": str(result.imageDate),
            "imageWidth": result.imageWidth,
            "imageHeight": result.imageHeight,
            "imageFile": result.imageFile
        }
        return {args["id"]: resultDict}
api.add_resource(APIImages, '/api/v1/images/')

if __name__ == "__main__":
    app.debug = True
    app.run()
