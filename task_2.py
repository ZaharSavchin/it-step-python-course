class Complex:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"{self.a}"

    def __add__(self, other):
        if isinstance(other, Complex):
            return self.a + other.a
        raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Complex):
            return self.a - other.a
        raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, Complex):
            return self.a * other.a
        raise NotImplementedError

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return self.a / other.a
        raise NotImplementedError

    def __abs__(self):
        return abs(self.a)


c0 = Complex(0)
c1 = Complex(10)
c2 = Complex(5)
c3 = Complex(-13)
print(c1 + c2)
print(c1 * c2)
print(c1 - c2)
print(c1 / c2)
print(c3)
print(abs(c3))