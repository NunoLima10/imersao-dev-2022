import os
import sqlite3

# Create a function to connect to a database with SQLite
class SQLite_Connector:

    def __init__(self, db_name='database/Scoreboards.db') -> None:
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.db_exit = False
        self.sqlite_connect()
        self.create_tables()
        
    def create_tables(self) -> None:
        
        if not self.db_exit:
            sql_file = open("database/bank_simulator.sql")
            sql_as_string = sql_file.read()
            self.cursor.executescript(sql_as_string)
            print("[INFO] All tables Created")

    def sqlite_connect(self) -> bool:
        """Connect to a database if exists. Create an instance if otherwise.
            Args:
                db_name: The name of the database to connect
            Returns:
                an sqlite3.connection object
        """
        print("[INFO] Start database connection")

        if os.path.isfile(f"./{self.db_name}"):
            self.db_exit = True

        try:
            # Create a connection
            conn = sqlite3.connect(self.db_name, check_same_thread=False)
        except sqlite3.Error:
            print("[ERROR] Database not found")
        finally:
            print("[INFO] Database created")
            self.connection = conn  
        
        self.cursor = self.connection.cursor()
    
    def execute_sql_query(self, query: str, apply_data_schema) -> list:
        results = self.cursor.execute(query)
        self.connection.commit()

        return apply_data_schema(results.fetchall())
    
    def close_db(self) -> None:
        self.connection.commit()
        self.connection.close()