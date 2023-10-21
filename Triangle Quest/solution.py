for i in range(1,int(input())):
    print(int(i * round(111111111, -(9-i))/10**(9-i)))