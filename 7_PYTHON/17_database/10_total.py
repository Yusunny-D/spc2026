import sqlite3

def connect_db():
    return sqlite3.connect('example.db')
    

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
Create Table If Not Exists users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL)
""")
    
    conn.commit()
    conn.close()

def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("insert into users (name, age) values (?, ?)", (name, age))
    conn.commit()
    conn.close()


def get_user():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("Select * from users")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("select * from users where name=?", (name,))
    user = cur.fetchone()
    conn.close()
    return user

def update_user(new_age, name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET age=? WHERE name=?", (new_age, name))
    conn.commit()
    conn.close()

def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name=?", (name, ))
    conn.commit()
    conn.close()

def delete_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=?", (id, ))
    conn.commit()
    conn.close()

def main():
    create_table()

    insert_user('Alice', 30)
    insert_user('Bob', 25)
    insert_user('Charlie', 35)

    print('사용자 조회')
    users = get_user()
    for user in users:
        print(user)

    update_user(40, 'Alice')
    update_user(33, 'Bob')

    print('두번째 조회')
    user = get_user_by_name('Alice')
    print(user)

    delete_user_by_name('Alice')

    print('세번째 조회')
    users = get_user()
    for user in users:
        print(user)
    
if __name__ == '__main__':
    main()