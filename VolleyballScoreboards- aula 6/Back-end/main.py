from flask import Flask,jsonify
from flask_cors import CORS
from flask_restful import Api,Resource

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)


class VolleyballScoreboards(Resource):
    def get(self):
        return jsonify({"data":"q"})

class VolleyballScoreboards_Api(Resource):
    @staticmethod
    def start() -> None:
        api.add_resource(VolleyballScoreboards,"/")
        app.run(host='0.0.0.0', port=3000,debug=True)

if __name__=="__main__":
    VolleyballScoreboards_Api.start()




