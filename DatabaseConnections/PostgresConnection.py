import psycopg2
import structlog

logger = structlog.get_logger()


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
            logger.info("Database successfully queried for all names.")

            return self.cursor.fetchall()
        finally:
            self.conn.close()

    def insertName(self, tabelName: str, name: str) -> None:
        try:
            self.cursor.execute(f"INSERT INTO '{tabelName}' (name) VALUES ('{name}')")
            logger.info(f"Successfully inserted {name} into {tabelName} ")

        finally:
            self.conn.close()
