import sqlite3

# 내 DB접근 및 관리용
class MyDatabase():
    # 객체 만들 때 자동 실행 (미리 DB연결(만들기))
    def __init__(self):
        self.db=sqlite3.connect('board.sqlite', check_same_thread=False)
        self.db.row_factory = sqlite3.Row

        self.cursor = self.db.cursor()
    
    # SQL 실행용 함수
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    # SELECT 실행 및 결과 가져오는 함수
    def execute_fetch(self, query, args={}):
        self.cursor.execute(query, args)
        result = self.cursor.fetchall()
        return result
    
    # COMMIT용 함수
    def commit(self):
        self.db.commit()
    
def init_db():
    print('초기화 코드 추가하기')
    return
    
if __name__ == '__main__':
    print('여기는 DB테스트')
    db = MyDatabase()
    
    db.execute("""CREATE TABLE IF NOT EXISTS board (id integer PRIMARY KEY AUTOINCREMENT, title varchar(50), message varchar(200))""")
    db.execute("INSERT INTO board(title, message) VALUES (?, ?)", ('title1', 'message1'))
    db.commit()
    result = db.execute_fetch('select * from board')
    print(result)
    db.execute('delete From board')
    db.commit()
