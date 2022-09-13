from flask import jsonify
from flask_restful import Resource,reqparse
from controllers.team import TeamController

add_new_args = reqparse.RequestParser()
add_new_args.add_argument("team_name",type=str,required=True,help="Team name is required.")
add_new_args.add_argument("games",type=int,required=True,help="Number of is  required.")
add_new_args.add_argument("victories",type=int,required=True,help="Number of is required.")
add_new_args.add_argument("defeats",type=int,required=True,help="Number of is required.")
add_new_args.add_argument("score",type=int,required=False,help="Number of is required.")

update_args = reqparse.RequestParser()
update_args.add_argument("team_name",type=str,help="Team name is optional.")
update_args.add_argument("games",type=int,help="Number of is  optional.")
update_args.add_argument("victories",type=int,help="Number of is optional.")
update_args.add_argument("defeats",type=int,help="Number of is optional.")
update_args.add_argument("score",type=int,help="Number of is optional.")

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
        args = update_args.parse_args()
        update_team = team_controller.update_team(
            id=id,
            team_name=args["team_name"],
            games=args["games"],
            victories=args["victories"],
            defeats=args["defeats"],
            score=args["score"]
        )
        return jsonify(update_team)

    def delete(self, id: int):
        return jsonify(team_controller.delete_team(id))