from connection import Connect


def CheckUser(username):
    conn = Connect()
    cursor = conn.cursor()
    cursor.execute('select * from  user_table;')

    for row in cursor.fetchall():
        if username in row:
            return True
        else:
            return False


CheckUser('Dumith')
