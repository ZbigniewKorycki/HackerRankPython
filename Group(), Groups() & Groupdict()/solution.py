import re

S = input()

m = re.findall(r'([a-zA-Z0-9])\1', S)

if m:
    print(m[0])
else:
    print(-1)