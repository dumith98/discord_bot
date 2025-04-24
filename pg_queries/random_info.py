import os
import psycopg2
import dotenv

dotenv.load_dotenv()

try:
    conn = psycopg2.connect(
                dbname=os.getenv('database'),
                    user=os.getenv('user'),
                        password=os.getenv('password'),
                            host=os.getenv('host')
                            )
    print('Database successfully connected!')

except:
    print('Connection failed!')

cursor = conn.cursor()

cursor.execute('select * from  user_table;')
print(cursor.fetchall())

conn.close()

# print(cursor.execute('SELECT * from teste'))    
