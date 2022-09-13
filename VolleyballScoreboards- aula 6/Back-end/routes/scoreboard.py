from flask import jsonify
from flask_restful import Resource

class Scoreboard(Resource):
    def get(self):
        return jsonify({"data":"Hello from Volleyball Scoreboards "})