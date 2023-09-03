pictures = [
    [0, 0,  0,  1,  0,  0,  0],
    [0, 0,  1,  1,  1,  0,  0],
    [0, 1,  1,  1,  1,  1,  0],
    [1, 1,  1,  1,  1,  1,  1],
    [0, 0,  0,  1,  0,  0,  0],
    [0, 0,  0,  1,  0,  0,  0],
    [0, 0,  0,  1,  0,  0,  0],
    [0, 0,  0,  1,  0,  0,  0]
    ]
for row in pictures:
    for pixel in row:
        if pixel == 0:
            print(" ", end="")
        elif pixel == 1:
            print("*", end='')
    print()















