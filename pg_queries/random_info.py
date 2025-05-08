def CheckUser():
    from connection import Connect

    conn = Connect()
    cursor = conn.cursor()
    cursor.execute('select * from  user_table;')

    users = 'Here is the list of names in my database: '

    for row in cursor.fetchall():
        users += f'{row[1]}\n'

    return users
print(CheckUser())
