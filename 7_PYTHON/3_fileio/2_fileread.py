# 작은 파일 읽기
with open('file.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print('파일 내용: ', data)

# file = open('file.txt', 'r', encoding='utf-8')
# data = file.read()
# file.close()

# print(data)

# 큰 파일 읽기
with open('file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print('파일 내용: ', line)