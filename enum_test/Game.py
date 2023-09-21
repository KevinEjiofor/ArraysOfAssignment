from random import random


# def game():
#     num = random(1, 10)
#     counter = 1
#     numbers = num
#
#     while counter < 10:
#         number = int(input("kindly a number: "))
#         if num == number:
#             print("you won")
#             break
#         else:
#             print("wrong entry")
#             if number == 4:
#                 print("Too low,try  again")
#             elif number == 7:
#                 print("Too high, try again")
#             if counter == 5:
#                  print("you have 5 more chance")
#     counter += 1

def game2():
    for counter in range(1, 101):
        if counter % 3 == 0 and counter % 5 == 0:
            print("Fizz_buzz")
        elif counter % 3 == 0:
            print("fizz")
        elif counter % 5 == 0:
            print("Buzz")
        else:
            print(counter)


if __name__ == '__main__':
    # game()
    game2()











