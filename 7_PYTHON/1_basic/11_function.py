def add_numbers(a, b):
    ''' 이 함수는 인자를 두 개 받아서 합을 변환하는 함수입니다. '''
    result = a + b
    return result

sum = add_numbers(3, 4)
print(f"두 수의 합은 {sum}입니다.")

def add_numbers2(a, b):
    return a, b, a+b

input1, input2, sum = add_numbers2(3, 4)
print(f'인자1은 {input1}, 인자2는 {input2}, 두 수의 합은 {sum}입니다.')

# def calculate_all(a, b):
#     addition = a + b
#     subtraction = a - b
#     multiplication = a*b
#     division = a / b


# add, sub, mul, div = calculate_all(3, 4)
# print(f'덧셈은 {add}, 뺄샘은 {sub}, 곱셈은 {mul}, 나눗셈은 {div}')

# add, _, mul, _ = calculate_all(3, 4)
# print(f'덧셈은 {add}, 곱셈은 {mul}')

def create_profile(name, age, city='서울', job='학생'):
    profile = f'이름 {name}, 나이: {age}, 지역: {city}, 직업: {job}'
    return profile

print(create_profile('홍길동', 23))
print(create_profile('김길동', 26))
print(create_profile('박길동', 29))
print(create_profile('이길동', 27, '부산'))
print(create_profile('전길동', 27, '부산', '직장인'))