import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

cur.execute('''
            Drop table users
            ''')

conn.commit()
conn.close()