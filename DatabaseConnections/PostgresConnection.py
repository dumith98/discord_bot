import psycopg2

from cogs.list_names_postgres_db import DataBaseConfig


class PostgresConnection:
    def __init__(self, database_config: DataBaseConfig) -> None:
        self.database = database_config.get("database")
        self.user = database_config.get("user")
        self.password = database_config.get("password")
        self.host = database_config.get("host")
        # self.database = database
        # self.user = user
        # self.password = password
        # self.host = host
        # self.conn = psycopg2.connect(
        #     dbname=database, user=user, password=password, host=host
        # )
        # self.cursor = self.conn.cursor()

    def getAllNames(self, tableName: str) -> list:
        """This method returns a list of tuples of each column"""
        try:
            self.cursor.execute(f"select * from  {tableName};")

            return self.cursor.fetchall()
        finally:
            self.conn.close()

    # TODO: implent  C of crud
    def insertName(self, tabelName: str, name: str) -> None:
        try:
            self.cursor.execute(f"INSERT INTO '{tabelName}' (name) VALUES ('{name}')")

        finally:
            self.conn.close()
