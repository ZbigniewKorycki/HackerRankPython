for i in range(1, int(input())+1):
    print(int(123456789/(10**(9-i)))*(10**(i-1))+int(987654321%(10**(i-1))))
