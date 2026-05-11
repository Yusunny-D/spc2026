my_list = [1, 2, 3, 4, 5]

print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[4])
# print(my_list[5])

print(my_list[-1])
print(my_list[-2])

print(my_list[1:3])
print(my_list[3:5])
print(my_list[:2])
print(my_list[2:])

# 원본 리스트에 멤버 추가하기
my_list.append(6)
print(my_list)

# 특정 위치에 멤버 추가하기
my_list.insert(2, 99)
print(my_list)

# 해당 값의 요소 삭제하기
my_list.remove(99)
print(my_list)

# 특정 인덱스의 요소 삭제하기
my_list.pop(3)
print(my_list)

my_list.pop() # 인덱스 안 넣으면 제일 뒤에 뺌

my_list.clear()
print(my_list)

my_list = [5, 2, 3, 1, 6, 7, 8, 4, 9]
my_list.sort()
print(my_list)
print(my_list) # sort()는 정렬하면서 원본 값을 변경함

my_list = [5, 2, 3, 1, 6, 7, 8, 4, 9]
new_list = sorted(my_list) # sorted는 원본을 유지하고 복제본을 만듦
print(my_list)
print(new_list)

copyed_list = my_list.copy() # 원본의 복제본을 만듦
print(copyed_list)
copyed_list.sort(reverse=True)
print(copyed_list)
print(my_list)

print('\n'+'-'*30)

# 리스트 컴프리헨션
numbers = [x for x in range(1, 10)]
print(numbers)
numbers = [x for x in range(5)]
print(numbers)
numbers = [x**2 for x in range(5)]
print(numbers)
numbers = [x for x in range(1, 10) if x%2 == 0]
print(numbers)
numbers = [x for x in range(1, 10) if x%2 == 1]
# numbers = [x             for x in range(1, 10)               if x%2 == 1]
print(numbers)

list1=[1, 2, 3]
list2=[4, 5, 6]

list12 = list1 + list2
print(list12)
print(list1*3)