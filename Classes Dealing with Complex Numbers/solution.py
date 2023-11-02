import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        result_addition = Complex(real=self.real + no.real, imaginary=self.imaginary + no.imaginary)
        return result_addition

    def __sub__(self, no):
        result_subtraction = Complex(real=self.real - no.real, imaginary=self.imaginary - no.imaginary)
        return result_subtraction

    def __mul__(self, no):
        mul_real = (self.real * no.real) - (self.imaginary * no.imaginary)
        mul_imaginary = (self.imaginary * no.real) + (self.real * no.imaginary)
        result_multiplication = Complex(mul_real, mul_imaginary)
        return result_multiplication

    def __truediv__(self, no):
        div_real = (self.real * no.real + self.imaginary * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        div_imaginary = (self.imaginary * no.real - self.real * no.imaginary) / (no.real ** 2 + no.imaginary ** 2)
        result_div = Complex(div_real, div_imaginary)
        return result_div

    def mod(self):
        mod_real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        mod_imaginary = 0
        result_mod = Complex(mod_real, mod_imaginary)
        return result_mod

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')