from flask import jsonify
from flask_restful import Resource,reqparse
from controllers.team import TeamController

add_new_args = reqparse.RequestParser()
add_new_args.add_argument("team_name",type=str,required=True,help="Team name is required.")
add_new_args.add_argument("games",type=int,required=True,help="Number of is  required.")
add_new_args.add_argument("victories",type=int,required=True,help="Number of is required.")
add_new_args.add_argument("defeats",type=int,required=True,help="Number of is required.")
add_new_args.add_argument("score",type=int,required=True,help="Number of is required.")

team_controller = TeamController()

class Teams(Resource):
    def get(self):
        return jsonify(team_controller.get_team())

    def post(self):
        args = add_new_args.parse_args()
        new_team = team_controller.create_new(
            team_name=args["team_name"],
            games=args["games"],
            victories=args["victories"],
            defeats=args["defeats"],
            score=args["score"]
        )
        return jsonify(new_team)


class Team(Resource):
    def get(self, id: int):
        return jsonify(team_controller.get_team(id))

    def put(self, id: int):
        pass

    def delete(self, id: int):
        pass