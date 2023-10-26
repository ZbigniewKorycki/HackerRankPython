from collections import defaultdict


n, m = list(map(int, input().split()))

d = defaultdict(list)

words_a = [input() for _ in range(n)]
words_b = [input() for _ in range(m)]

for index, word in enumerate(words_a, 1):
    if word in words_b:
        d[word].append(index)


for word in words_b:
    if not d[word]:
        print("-1")
    else:
        print(*d[word])




