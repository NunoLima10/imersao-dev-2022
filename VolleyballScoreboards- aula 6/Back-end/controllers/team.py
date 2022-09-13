from  database.db_connector import SQLite_Connector
from schemas.schemas import Schemas
class TeamController(SQLite_Connector):
    def __init__(self, db_name='database/scoreboard.db') -> None:
        super().__init__(db_name)


    def get_team(self, id: int = None):
        if id:
           sql_query = f"SELECT * FROM team WHERE id={id}"
        else:
            sql_query= f"SELECT * FROM team"
        
        return self.execute_sql_query(sql_query,Schemas.team)

    def create_new(self, team_name: str , games: int, 
                victories: int, defeats: int, score: int):
        sql_query = f"""
            INSERT INTO team(team_name, games, victories, defeats, score)
            VALUES('{team_name}', {games}, {victories}, {defeats}, {score});
        """
        try:
            self.execute_sql_query(sql_query,Schemas.team)
        except Exception as error:
            print(error)
        return self.get_team()[-1]
    
    def update_team(self, **kwargs):
        update_list = [
            f'team_name="{kwargs["team_name"]}"' if kwargs["team_name"] else '',
            f'games={kwargs["games"]}' if kwargs["games"] else '',
            f'victories={kwargs["victories"]}' if kwargs["victories"] else '',
            f'defeats={kwargs["defeats"]}' if kwargs["defeats"] else '',
            f'score={kwargs["score"]}' if kwargs["score"] else '',
        ]
        update_list = [value for value in update_list if value!='']
        sql_query = f"""
            UPDATE team SET
            {",".join(update_list)}
            WHERE id={kwargs["id"]}
        """
        try:
            self.execute_sql_query(sql_query,Schemas.team)
        except Exception as error:
            print(error)
        return self.get_team(kwargs["id"])

    def delete_team(self, id: int):
        sql_query = f"DELETE FROM team WHERE id={id}"

        self.execute_sql_query(sql_query, Schemas.team)
        return {"data":"Successfully deleted"}

