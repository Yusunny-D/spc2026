def numbers():
    for i in range(100000):
        yield i

for num in numbers():
    print(num)
    if num >= 5:
        break