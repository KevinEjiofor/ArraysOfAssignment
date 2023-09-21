import math


def circle(radius):
    are_of_circle = math.pi * (radius ** 2)

    if radius < 0:
        raise ValueError("value is less than O")

    if type(radius) != int and type(radius) != float:
        raise  TypeError("radius would  be a number above 0")

    return are_of_circle





