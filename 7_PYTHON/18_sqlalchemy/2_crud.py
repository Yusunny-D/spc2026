from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')

# 객체 정의
Base = declarative_base()

# 테이블 정의
class User(Base):
    __tablename__ = 'users' # 안쓰면 클라스명이 테이블명
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# 실행
Base.metadata.create_all(engine)

# CRUD 수행할 함수 구현
def create_user(session, name, age):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    return new_user

def list_users(session):
    users = session.query(User).all()
    return users

def get_user_by_id(session, user_id):

    # 원래하던 직관적인 스타일
    # user = session.query(User).filter_by(id=user_id).first()
    # return user

    return session.get(User, user_id)

def update_user_age(session, user_id, new_age):
    user = session.get(User, user_id)
    if not user:
        return False
    user.age = new_age
    session.commit()
    return True

def delete_user_by_id(session, user_id):
    user = session.get(User, user_id)
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True

def delete_user_by_name(session, name):
    users = session.query(User).filter_by(name=name).all()
    if not users:
        return 0
    for user in users:
        session.delete(user)
        session.commit()
    return len(users)

if __name__=="__main__":
    Session = sessionmaker(bind=engine)
    with Session() as session:
        hong = create_user(session, "홍길동", 25)
        go = create_user(session, "고길동", 33)

        print(f'추가된 사용자들: {hong.id}, {go.id}')

        user = get_user_by_id(session, hong.id)
        print(f'조회한 사람은: {user.id}, {user.name}')

        users = list_users(session)
        print('전체 사용자 조회')
        for u in users:
            print(f'- {u.id}: {u.name}, {u.age}')

        # 사용자 정보 수정
        update_user = update_user_age(session, go.id, 44)
        user = get_user_by_id(session, go.id)
        print(f'조회한 사람은: {user.id}, {user.name}, {user.age}')

        users = list_users(session)
        print('전체 사용자 조회')
        for u in users:
            print(f'- {u.id}: {u.name}, {u.age}')

        # 사용자 삭제
        delete_user_count = delete_user_by_name(session, '홍길동')
        print(f'삭제된 사용자 수는: {delete_user_count}')

        users = list_users(session)
        print('전체 사용자 조회')
        for u in users:
            print(f'- {u.id}: {u.name}, {u.age}')

