def square(x):
    return x ** 2


Rain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

v = [i for i in Rain if i % 2 == 0]

print(v)

print(list(map(square, Rain)))

# Rain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# result = ([i ** 2 for i in Rain])
# print(result)
