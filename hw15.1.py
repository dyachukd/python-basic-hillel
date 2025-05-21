import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()
        side = math.isqrt(total_area)
        while total_area % side != 0:
            side -= 1
        new_width = side
        new_height = total_area // side
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        if n <= 0:
            raise ValueError("Множник має бути додатнім числом")
        new_area = self.get_square() * n
        side = math.isqrt(int(new_area))
        while int(new_area) % side != 0:
            side -= 1
        new_width = side
        new_height = int(new_area) // side
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"
