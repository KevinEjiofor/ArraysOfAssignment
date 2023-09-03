from Array.enum_geopolitical_zones import Point


class Point:
    color = "blue"

    def __init__(self,point_a, point_b):
        self.__point_a = point_a
        self.__point_b = point_b

    @property
    def point_b(self):
        return self.__point_b

    @point_b.setter
    def point_b(self, value):
        if value < 0:
            return ValueError("value cannot be negative")
        self.__point_b = value
    @property
    def point_a(self):
        return self.__point_a

    @point_a.setter
    def point_a(self, value):
        if value < 0:
            return ValueError("value cannot be negative")
        self.__point_a = value

    def draw(self):
        print(f"drawing from point {self.__point_a} to {self.__point_b}")


    def __str__(self):
        return f"({self.__point_a},{self.__point_b})"


    def __eq__(self, other):
        return self.__point_a == other.point_a and self.__point_b == other.point_b

    def __add__(self, other):
        return self.point_a + other.point_a , self.point_b + other.point_b



Point.color = "red"
p1 = Point(1, 2)
p2 = Point(1, 2)
total = p1.__add__(p2)

print(total)

print(p1.point_a)
print(p2.color)
# class Address:
#   def __init__(mine, street, number):
#     mine.street = street
#     mine.number = number
#
#   def myfunc(abc):
#     print("My Address is " + abc.street)
#
# p1 = Address("Albert Street", 20)
# p1.myfunc()
