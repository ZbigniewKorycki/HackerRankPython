x, k = input().split()
polynomial = input()

polynomial = polynomial.replace("x", str(x))
polynomial = polynomial.replace("x**2", f"{str(x)}**2")
polynomial = polynomial.replace("x**3", f"{str(x)}**3")

print(eval(polynomial) == int(k))
