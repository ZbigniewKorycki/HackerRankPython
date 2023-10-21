def minion_game(string):
    points_kevin = 0
    points_stuart = 0

    for index, letter in enumerate(string.upper(), 0):
        if letter in "AEIOU":
            points_kevin += len(string) - index
        else:
            points_stuart += len(string) - index
    if points_kevin < points_stuart:
        print("Stuart", points_stuart)
    elif points_kevin > points_stuart:
        print("Kevin", points_kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)