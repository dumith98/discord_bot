import os
import psycopg2
import dotenv

dotenv.load_dotenv()

def Connect():
    try:
        conn = psycopg2.connect(
                    dbname=os.getenv('database'),
                        user=os.getenv('user'),
                            password=os.getenv('password'),
                                host=os.getenv('host')
                                )
        print('\nDatabase successfully connected!\n')

        return conn

    except:
        print('Connection failed!')

