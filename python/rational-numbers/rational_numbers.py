from __future__ import division
from math import gcd

class Rational(object):
    def __init__(self, numerator, denominator):
        self.gcd = gcd(numerator,denominator)
        self.numerator = abs(int(numerator/self.gcd))
        self.denominator = abs(int(denominator/self.gcd))
        if numerator == 0:
            self.denominator = 1
        if numerator * denominator < 0:
            self.numerator *= -1
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __repr__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        resultNumerator = self.numerator * other.denominator + other.numerator * self.denominator
        resultDenominator = self.denominator * other.denominator
        return Rational(resultNumerator, resultDenominator)

    def __sub__(self, other):
        resultNumerator = self.numerator * other.denominator - other.numerator * self.denominator
        resultDenominator = self.denominator * other.denominator
        return Rational(resultNumerator, resultDenominator)

    def __mul__(self, other):
        resultNumerator = self.numerator * other.numerator
        resultDenominator = self.denominator * other.denominator
        return Rational(resultNumerator, resultDenominator)


    def __truediv__(self, other):
        resultNumerator = self.numerator * other.denominator
        resultDenominator = self.denominator * other.numerator
        return Rational(resultNumerator, resultDenominator)

    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    def __pow__(self, power):
        powerAbs= abs(power)
        if power<0:
            resultNumerator = self.denominator ** powerAbs
            resultDenominator = self.numerator ** powerAbs
        else:
            resultNumerator = self.numerator ** powerAbs
            resultDenominator = self.denominator ** powerAbs
        return Rational(resultNumerator,resultDenominator)

    def __rpow__(self, base):
        return (base**self.numerator)**(1/self.denominator)
