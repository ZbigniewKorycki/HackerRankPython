import string

alphabet = list(string.ascii_lowercase)
alphabet_joined = '-'.join(alphabet)
reversed_alphabet_joined = '-'.join(alphabet[::-1])
size = int(input())

def draw_rangoli(size):
    if size == 1:
        print(alphabet[0])
    else:
        for x in range(size):
            print(reversed_alphabet_joined[
                  (len(reversed_alphabet_joined) - 1) - (size - 1) * 2:(len(reversed_alphabet_joined) - 1) - (
                          size - 1) * 2 + 2 * x].rjust((size - 1) * 2, '-'), end='')
            print(alphabet[size - x - 1], end='-')
            print(alphabet_joined[(size - 1) * 2 - 2 * x + 2:(size - 1) * 2 + 1].ljust(
                ((size - 1) * 2 - 1), '-'))

        for x in range(1, size):
            print(reversed_alphabet_joined[
                  (len(reversed_alphabet_joined) - 1) - (size - 1) * 2:(len(reversed_alphabet_joined) - 1) - 2 * x].
                  rjust((size - 1) * 2, '-'), end='')
            print(alphabet[x], end='-')
            print(alphabet_joined[2 + x * 2:(size) * 2].ljust(((size - 1) * 2 - 1), '-'))


draw_rangoli(size)
