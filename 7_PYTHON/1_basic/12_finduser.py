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
    '''이름 또는 나이를 입력받아 매칭되는 사람을 반환한다.'''
    found_users = []
    for user in users:
        if name:
            if user['name'] == name:
                found_users.append(user)
                return found_users
        else:
            if user['age'] == age:
                found_users.append(user)
                return found_users

print(find_users2('김민수'))

print('\n', '-'*30)

search_condition = {
    'name': '김민수'
}

def find_user2_best(condition):
    found = []
    for user in users:
        if user.get('name') == condition.get('name', '') and \
        user.get('age') == condition.get('age', 0) and \
        user.get('location') == condition.get('location', '')
        found.append(user)

    return found




