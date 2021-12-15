import math

class Sphere:

    __slots__ = ["__radius"]

    def __init__(self, radius):

        self.__radius = radius
    
    def get_radius(self):
        return self.__radius
    
    def get_circumferences(self):
        return 2*math.pi*self.__radius
    def get_surface_area(self):
        return 4*math.pi*self.__radius**2
    
    def get_volume(self):
        return (4/3)*math.pi*self.__radius ** 3
    
def main():
    
    print(Sphere(8))

main