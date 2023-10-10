cube = lambda x: x ** 3

def fibonacci(n):
    fibonacci_numbers = []
    for num in range(n):
        if num == 0 or num == 1:
            fibonacci_numbers.append(num)
        else:
            number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
            fibonacci_numbers.append(number)
    return fibonacci_numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
