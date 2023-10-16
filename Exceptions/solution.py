cases_number = int(input())

def print_result_of_error(cases):
    for _ in range(cases):
        a, b = input().split()

        try:
            result = int(a)//int(b)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as ev:
            print("Error Code:", ev)
        else:
            print(result)


if __name__ == "__main__":
    print_result_of_error(cases_number)