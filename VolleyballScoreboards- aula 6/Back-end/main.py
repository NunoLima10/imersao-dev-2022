from flask import Flask
from flask_cors import CORS
from flask_restful import Api,Resource

from routes.team import Teams,Team
from routes.scoreboard import Scoreboard

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
class VolleyballScoreboards_Api(Resource):
    @staticmethod
    def start() -> None:
        api.add_resource(Scoreboard,"/")
        api.add_resource(Teams,"/teams")
        api.add_resource(Team,"/team/<int:id>")

        app.run(host='0.0.0.0', port=3000,debug=True)

if __name__=="__main__":
    VolleyballScoreboards_Api.start()




