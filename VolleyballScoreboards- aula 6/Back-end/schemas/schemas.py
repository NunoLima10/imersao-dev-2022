class Schemas:
    @staticmethod
    def team(data: tuple) -> list:
        return [
            {
                "id":dt[0],
                "team_name": dt[1],
                "games":dt[2],
                "victories": dt[3],
                "defeats":dt[4],
                "score":dt[5]
            }for dt in data]
