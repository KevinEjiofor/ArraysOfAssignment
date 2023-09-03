# def square():
#     return number ** 2
#
#
# number = int(input("enter number: "))
# print(square())

# def multiple(number=int(input("enter number:"))):
#     print(f"""
#     {number} * 1  = {number * 1}
#     {number} * 2  = {number * 2}
#     {number} * 3  = {number * 3}
#     {number} * 4  = {number * 4}
#     {number} * 5  = {number * 5}
#     {number} * 6  = {number * 6}
#     {number} * 7  = {number * 7}
#     {number} * 8  = {number * 8}
#     {number} * 9  = {number * 9}
#     {number} * 10 = {number * 10}
#     {number} * 11 = {number * 11}
#     {number} * 12 = {number * 12}""")
#
#
# print(multiple())


def number():
    num = int(input("Enter a number: "))
    for i in range(1, 13):
        for x in range(1, num + 1):
            print(f"{x} X {i} = {i * x:<20}",end=" \t")
        print()


number()
