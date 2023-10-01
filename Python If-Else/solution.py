def check_number(number):
    if 1 <= number <= 100:
        if number % 2 != 0:
            print("Weird")
        elif number in range(2, 6):
            print("Not Weird")
        elif number in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")


if __name__ == '__main__':
    n = int(input("Number: ").strip())
    check_number(n)

