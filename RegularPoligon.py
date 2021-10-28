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
