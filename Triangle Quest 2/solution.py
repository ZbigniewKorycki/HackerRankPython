for i in range(1, int(input())+1):
    print(''.join(list(map(str, [*range(1, i)]))), ''.join(list(map(str, [*range(i,0, -1)]))), sep='')