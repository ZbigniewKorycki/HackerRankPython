import cmath
import math

complex_z = input()
phase_z = cmath.phase(complex(complex_z))
modulus_fi = abs(phase_z)
x, y = complex_z.split("+")         #input in format 1+2j

x = int(x.strip())
y = int(y.replace("j", "").strip())

r = math.sqrt(x**2 + y**2)

print(r)
print(modulus_fi)