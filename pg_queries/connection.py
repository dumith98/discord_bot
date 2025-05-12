import os
import psycopg2
import dotenv


class PostgresConnection:
    def __init__(self, database, user, password, host) -> None:
        self.database = database
        self.user = user
        self.password = password
        self.host = host

    def connect(self):
        dotenv.load_dotenv()
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("database"),
                user=os.getenv("user"),
                password=os.getenv("password"),
                host=os.getenv("host"),
            )
            print("\nDatabase successfully connected!\n")

            return conn

        except:
            print("Connection failed!")

    def getAllNames(self) -> list:
        """This method returns a lsit of tuples of each column"""
        cursor = self.connect().cursor()
        cursor.execute("select * from  user_table;")

        return cursor.fetchall()


postgres = PostgresConnection(
    os.getenv("database"), os.getenv("user"), os.getenv("password"), os.getenv("host")
)
postgres.connect()
print(postgres.getAllNames())
