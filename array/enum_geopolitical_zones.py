from enum import Enum
import re


class geopolitical_zone(Enum):

        NORTH_CENTRAL = "Benue", "Abuja", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau"
        NORTH_EAST =    "Adamawa", "Bauchi", "Borno","Gombe","Taraba", "Yobe"
        NORTH_WEST =    "Kaduna" , "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"
        SOUTH_WEST =    "Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"
        SOUTH_EAST =     "Abia", "Anambra", "Ebonyi", "Enugu", "Imo"
        SOUTH_SOUTH =      "Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "Rivers"

def user():
    state = input("\nkindly enter state: ")
    if re.search("^(?!$)\D+$",state):
        if state.capitalize() in geopolitical_zone.SOUTH_SOUTH.value:
            print("SOUTH SOUTH")
        elif state.capitalize() in geopolitical_zone.NORTH_CENTRAL.value:
            print("NORTH CENTRAL")
        elif state.capitalize() in geopolitical_zone.NORTH_WEST.value:
            print("NORTH WEST")
        elif state.capitalize() in geopolitical_zone.NORTH_EAST.value:
         print("NORTH EAST")
        elif state.capitalize() in geopolitical_zone.SOUTH_WEST.value:
            print("SOUTH WEST")
        elif state.capitalize() in geopolitical_zone.SOUTH_EAST.value:
            print("SOUTH EAST")
    else:
            print("\nThis is not a state ")
            user()


class Point:
    def __init__(self, z,g):
        self.z = z
        self.g = g

    def draw(self):
        print(f"drawing from point {self.z}to{self.g}")


    def __str__(self):
        return f"{self.z},{self.g}"



if __name__ == '__main__':
    user()
