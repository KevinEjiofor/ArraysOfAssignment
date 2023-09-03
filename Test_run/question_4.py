import math


def user():
    entry = float(input("Enter radius: "))
    return  math.pi * (entry ** 2)

if __name__ == '__main__':
    result = user()
    print("result : ", f'{result:.2f}')