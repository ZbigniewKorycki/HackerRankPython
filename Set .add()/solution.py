N = int(input())

countries = set()
for stamp in range(0, N):
    country = input()
    countries.add(country)

print(len(countries))
