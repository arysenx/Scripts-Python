import math
class RegularPoligon():

    def __init__(self, base, n = 3): 
        self.base = base
        self.n = n
    
    def __str__(self):
        return "Soy un polígono regular de {} lados de longitud {}".format(self.n, self.base)

    @property
    def apothem(self):
        return self.base / (2*round(math.pi / self.n),3)

    @property
    def perimeter(self):
        return self.n * self.base
    
    @property
    def area(self):
        return self.apothem * self.perimeter / 2

class Triangle(RegularPoligon):
    def __init__(self, base):
        super().__init__(base, 3)

class Square(RegularPoligon):
    def __init__(self, base):
        super().__init__(base, 4)

class Pentagon(RegularPoligon):
    def __init__(self, base):
        super().__init__(base, 5)

class Tetrahedron(Triangle):
    def __str__(self):
        return "Soy un tetraedro con lados de longitud {}".format(self.base)
    @property
    def area(self):
        return 4*super().area
    
    @property
    def volume(self):
        return math.sqrt(2) / 12 * self.base

class Cube(Square):
    def __str__(self):
        return "Soy un cubo con lados de longitud {}".format(self.base)
    
    @property
    def area(self):
        return 6 * super().area
    @property
    def volume(self):
        return super().area*self.base

class Circle():
    def __init__(self, r):
        self.rad = r

    def __str__(self):
        return "Soy un círculo de radio {}".format(self.rad)
    
    @property
    def diameter(self):
        return 2*self.rad
    
    @property
    def perimeter(self):
        return self.diameter * math.pi

    @property
    def area(self):
        return math.pi * self.rad ** 2

class Cylinder(Circle, Square):
    def __init__(self, r):
        super().__init__(r)
        self.height = super().perimeter

    def __str__(self):
        return "Soy un cilindro de altura {} y radio {}".format(round(self.height,3),self.rad)
    
    @property
    def area(self):
        lateral_area = self.height**2
        base_area = super().area
        return 2 * base_area + lateral_area
    
    @property
    def volume(self):
        base_area = super().area
        return base_area * self.height

s = RegularPoligon(2, 4)
print(s.area)