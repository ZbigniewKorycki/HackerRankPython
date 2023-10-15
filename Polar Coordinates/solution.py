import cmath
import math

complex_z = input()
phase_z = cmath.phase(complex(complex_z))
modulus_fi = abs(phase_z)

complex_z = complex_z.replace("-", " ")
complex_z = complex_z.replace("+", " ")
complex_z = complex_z.replace("j", " ")
complex_z = complex_z.strip()
x, y = complex_z.split()

r = math.sqrt(int(x)**2 + int(y)**2)

print(round(r,3))
print(round(phase_z, 3))
