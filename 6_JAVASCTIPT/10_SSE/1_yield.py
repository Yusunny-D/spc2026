# 우리가 하고 싶은 것: 서버에서 바뀌는 데이터를 알아서 반환
# 아래 처럼
# def test():
#     return 1
#     return 2
#     return 3

# x = test()

# print(x)

def test():
    yield 1
    yield 2
    yield 3

x = test()
print(next(x))
print(next(x))
print(next(x))