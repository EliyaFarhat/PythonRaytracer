import math


class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return print(f"{self.x}, {self.y}, {self.z}")

    def dotProduct(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def magnitude(self):
        # Uses itself to get magnitude
        return math.sqrt(self.dotProduct(self))

    def normalize(self):
        return self / self.magnitude()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        # Ensure that other is a NUMBER not VECTOR
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        # Ensure that other is a NUMBER not VECTOR
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)