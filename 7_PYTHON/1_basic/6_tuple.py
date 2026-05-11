# 튜플 (읽기 전용 리스트)
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(my_list)
print(my_tuple)

print(my_list[2])
print(my_tuple[2])

my_list[2] = 99
# my_tuple[2] = 99 이건 안됨

print(my_list[-1])
print(my_tuple[-1])

print(my_list[3:5])
print(my_tuple[3:5])

print(my_list[0:1])
print(my_tuple[0:1]) # (1) 아니고 (1,)인 이유는 명시적으로 튜플을 알려주기 위해서...

# 튜플의 값을 쓰고 싶으면?
my_newlist = list(my_tuple) # 타입 변환 후 복제본 만들기
print(my_newlist)

my_newlist[2] = 88

print(my_newlist)
print(my_tuple)


my_newtuple = tuple(my_list)
print(my_newtuple)

my_list[2] = 77

print(my_newtuple)
print(my_list)

print('\n'+'-'*30)

a, b, c= (1, 2, 3) # 튜플 언 패킹 () 튜블로 감싸져 있는 걸 분해
print(a, b, c)

a_person = ("John", 23, "Student")
print(a_person)
name, age, occ = a_person
print(name)
print(age)