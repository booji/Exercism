import math

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(
                self.real + other.real,
                self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(
                self.real*other.real-self.imaginary*other.imaginary,
                self.real*other.imaginary+other.real*self.imaginary)

    def __sub__(self, other):
        return ComplexNumber(
                self.real - other.real,
                self.imaginary - other.imaginary)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imaginary**2
        real = self.real * other.real + self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real - self.real * other.imaginary
        return ComplexNumber(real/denom, imaginary/denom)

    def __abs__(self):
        return math.sqrt(self.real**2+self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(
                math.exp(self.real)*math.cos(self.imaginary),
                math.exp(self.real)*math.sin(self.imaginary))

    def __eq__(self,other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __repr__(self):
        return f"{self.real} + {self.imaginary}i"
