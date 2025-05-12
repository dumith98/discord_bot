import os
import psycopg2
import dotenv


class PostgresConnection:
    def __init__(self, database, user, password, host) -> None:
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.conn = psycopg2.connect(
            dbname=database, user=user, password=password, host=host
        )
        self.cursor = self.conn.cursor()

    def getAllNames(self, tableName: str) -> list:
        """This method returns a list of tuples of each column"""
        try:
            self.cursor.execute(f"select * from  {tableName};")

            return self.cursor.fetchall()
        finally:
            self.conn.close()

    def insertName(self, tabelName: str, name: str) -> None:
        try:
            self.cursor.execute(f"INSERT INTO '{tabelName}' (name) VALUES ('{name}')")

        finally:
            self.conn.close()

#############   TESTING DB CONNECTION ##############
import dotenv

dotenv.load_dotenv()


postgres = PostgresConnection(
    os.getenv("database"), os.getenv("user"), os.getenv("password"), os.getenv("host")
)
print(postgres.getAllNames("user_table"))
