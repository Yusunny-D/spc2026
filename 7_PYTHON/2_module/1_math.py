import math

print(math.pi)
print(math.e)
print(math.sqrt(16))
print(math.sin(5))
print(math.sin(8))
print(math.sin(math.pi))

print('\n', '-'*30)
import datetime as dt

print(dt.datetime.now())
print(dt.datetime.now().strftime('%y-%m-%d'))
print(dt.datetime.now().strftime('%H-%M-%S'))

a_day = dt.datetime(2025, 1, 1, 10, 00, 0)
b_day = dt.datetime(2025, 1, 1)
print(a_day)
print(b_day)

print('\n', '-'*30)
import random

print(random.random())
print(math.floor(random.random() * 100))
print(random.randint(1, 100))

print('\n', '-'*30)
def roll_dice():
    my_number = random.randint(1, 6)
    return my_number

print('내 주사위의 숫자는: ', roll_dice())
print('내 주사위의 숫자는: ', roll_dice())
print('내 주사위의 숫자는: ', roll_dice())
print('내 주사위의 숫자는: ', roll_dice())
print('내 주사위의 숫자는: ', roll_dice())
print('내 주사위의 숫자는: ', roll_dice())
print('내 주사위의 숫자는: ', roll_dice())

fruits = ["사과", "바나나", "오렌지", "포도", "딸기", "수박"]

def pick_fruit():
    my_number = random.randint(0, len(fruits) - 1)
    my_pick = fruits[my_number]
    return my_pick

def pick_fruit2():
    return random.choice(fruits)

print("내 과일은: ", pick_fruit2())
print("내 과일은: ", pick_fruit2())
print("내 과일은: ", pick_fruit2())
print("내 과일은: ", pick_fruit2())
print("내 과일은: ", pick_fruit2())
print("내 과일은: ", pick_fruit2())