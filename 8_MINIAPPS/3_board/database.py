import sqlite3

class MyDatabase():
    def __init__(self):
        self.db=sqlite3.connect('board.sqlite', check_same_thread=False)
        self.db.row_factory = sqlite3
        self.cursor = self.db.cursor()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def execute_fetch(self, query, args={}):
        self.cursor.execute(query, args)
        result = self.cursor.fetchall()
        return result
    
if __name__ == '__main__':
    print('여기는 DB테스트')
    db = MyDatabase()
    
    db.execute("""CREATE TABLE board (id integer PRIMARY KEY AUTOINCREMENT, title varchar(50), message varchar(200))""")
    db.execute("INSERT INTO board(title, message) VALUES (?, ?)", ('title1', 'message1'))
    db.commit()
    result = db.execute_fetch('select * from board')
    print(result)
    db.execute('delete From board')
