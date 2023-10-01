if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().strip().split()))[:n]
    t = tuple(x)
    print(hash(t))