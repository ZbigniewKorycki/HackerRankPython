for i in range(1, int(input())+1):
    print(sum(d * 10**n for n,d in enumerate([*range(1, i)] + [*range(i,0, -1)])))