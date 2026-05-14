users = [
    {"name": "김민수", "age": 24, "location": "서울", "car": "아반떼"},
    {"name": "이지은", "age": 28, "location": "부산", "car": "K5"},
    {"name": "박서준", "age": 31, "location": "인천", "car": "쏘나타"},
    {"name": "최하린", "age": 22, "location": "대구", "car": "레이"},
    {"name": "정도윤", "age": 35, "location": "광주", "car": "싼타페"},
    {"name": "김예은", "age": 27, "location": "대전", "car": "모닝"},
    {"name": "조시우", "age": 29, "location": "울산", "car": "투싼"},
    {"name": "윤유진", "age": 24, "location": "수원", "car": "캐스퍼"},
    {"name": "한현우", "age": 33, "location": "고양", "car": "그랜저"},
    {"name": "오채원", "age": 26, "location": "성남", "car": "셀토스"}
]

def find_user_and_print(name):
    for user in users:
        # if user['name'] == name:
        if user['name'].startswith(name):
            print(user)

find_user_and_print('김')

print('\n', '-'*30)

def find_user_and_retun(name):
    found = [] # 찾은 사용자를 담을 리스트
    for user in users:
        # if user['name'] == name:
        if user['name'].startswith(name):
            found.append(user)
    return found

found_user = find_user_and_retun('구')
print(found_user)

def find_users2(name:str=None, age:int=None):
    # find_user2(나이) 이렇게 넣어서 찾고 싶은데
    # 파이썬은 2이상의 인자를 받는 함수면 아무 설명없이 인자를 넣으면
    # 첫번째 인자로 인식 => 그러니까 name=(나이) 이렇게 들어가버림
    # 그래서 나이만 넣고 싶으면 find_user2(age=나이) 이렇게 써야함
    # 아니면 로직 안에서 이름과 나이를 따로 구별하는 로직을 만들어야함
    '''
        이름 또는 나이를 입력받아 매칭되는 사람을 반환한다.
        => 이름과 나이, 이름, 나이 이렇게 3가지 방법으로 인자를 받을 수 있음
    '''
    found_users = []
    for user in users:
        if name is not None and age is not None:
            # 이름과 나이를 같이 받았을 때
            if user['name'] == name and user['age'] == age:
                # 이름과 나이가 같이 users에 있으면(이름과 나이가 불일치하면 안됨)
                found_users.append(user)
                return found_users
        elif name is not None:
            # 이름을 받았을 때
            if user['name'] == name:
                found_user.append(user)
        elif age is not None:
            # 나이를 받았을 때
            if user['age'] == age:
                found_users.append(user)
    
    return found_users

# print(find_users2('김민수'))

print('\n', '-'*30)

def find_users2_better(name=None, age=None, location=None):
    found_user = []
    for user in users:
        # true or 비교문
        if name is None or user['']


def find_user2_best(condition):
    found = []
    for user in users:
        if user.get('name') == condition.get('name', '') and \
        user.get('age') == condition.get('age', 0) and \
        user.get('location') == condition.get('location', '')
        found.append(user)

    return found



print('\n', '-'*30)

search_condition = {
    'name': '김민수'
}

