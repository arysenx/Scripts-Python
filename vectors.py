import math

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)

    @property
    def module(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def scalar_prod(self, num = 1):
        self.x *= num
        self.y *= num

    def extend_to_3D(self,z = 0):
        return Vector3D(self.x,self.y,z)

    @classmethod
    def sum(cls, vector1, vector2):
        return cls(vector1.x + vector2.x, vector1.y + vector2.y)

    @classmethod
    def subtract(cls, vector1, vector2):
        return cls(vector1.x - vector2.x, vector1.y - vector2.y)

    @staticmethod
    def dot_product(vector1, vector2):
        return vector1.x * vector2.x + vector1.y * vector2.y

    @classmethod
    def distance(cls,vector1, vector2):
        return cls.subtract(vector1,vector2).module

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def __str__(self):
        return "({},{},{})".format(self.x,self.y,self.z)

    @property
    def module(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def scalar_prod(self, num=1):
        super().scalar_prod(num=num)
        self.z *= num
    
    @classmethod
    def sum(cls, vector1, vector2):
        return cls(vector1.x + vector2.x, vector1.y + vector2.y, vector1.z + vector2.z)

    @classmethod
    def subtract(cls, vector1, vector2):
        return cls(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)

    """
    Distance no hace falta programarlo ya que lo hereda diréctamente
    de Vector2D
    """

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)   

    @classmethod
    def horizontal(cls):
        return cls(1, 0, 0)

    @classmethod
    def vertical(cls):
        return cls(0, 1, 0)

    @classmethod
    def forward(cls):
        return cls(0, 0, 1)

    @staticmethod
    def dot_product(vector1, vector2):
        return super().dot_product(vector1, vector2) + vector1.z * vector2.z

    

