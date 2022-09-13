CREATE TABLE IF NOT EXISTS team(
    id INTEGER PRIMARY KEY,
    team_name VARCHAR(15) NOT NULL,
    games INTEGER,
    victories INTEGER,
    defeats INTEGER,
    score INTEGER
);
