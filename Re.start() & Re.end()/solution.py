import re

s = input()
k = input()

list_matches = []
for letter in range(len(s)):
    m = re.search(f'^{k}', s[letter: len(s)])
    if m:
        list_matches.append((m.start()+letter, m.end()-1+letter))
if len(list_matches) == 0:
    print((-1, -1))
else:
    for x in set(list_matches):
        print(x)
