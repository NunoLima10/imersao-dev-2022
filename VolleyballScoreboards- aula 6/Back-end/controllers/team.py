from  database.db_connector import SQLite_Connector
from schemas.schemas import Schemas

class TeamController(SQLite_Connector):
    def __init__(self, db_name='database/Scoreboards.db') -> None:
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
    
    def update_team(self, id: int):
        pass

    def delete_team(self, id: int):
        pass

