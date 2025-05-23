from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")
        if abs(a) >= abs(b):
            raise ValueError("Це не правильний дріб (чисельник має бути менший за знаменник)")
        self.a = a
        self.b = b

    def _common_denominator(self, other):
        lcm = self.b * other.b // gcd(self.b, other.b)
        return (
            self.a * (lcm // self.b),
            other.a * (lcm // other.b),
            lcm
        )

    def __add__(self, other):
        a1, a2, common_b = self._common_denominator(other)
        return Fraction(a1 + a2, common_b)

    def __sub__(self, other):
        a1, a2, common_b = self._common_denominator(other)
        return Fraction(a1 - a2, common_b)

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тести
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
