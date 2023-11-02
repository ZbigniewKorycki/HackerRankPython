import re

S = input()

for letter in range(len(S)):
    word = S[letter:]
    m = re.match(r'([a-zA-Z0-9])\1', word)
    if m:
        print(S[letter])
        break
    elif letter == len(S) - 1:
        print(-1)
