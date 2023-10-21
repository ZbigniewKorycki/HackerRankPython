import time

def minion_game(string):
    points_kevin = 0
    score_stuart = 0
    string_len = len(string)
    for word_len in range(1, string_len+1):
        for letter_index in range(string_len - word_len + 1):
            word = string[letter_index:letter_index+word_len]
            if word[0] in "AEIOU":
                points_kevin += 1
            else:
                score_stuart += 1

    if points_kevin < score_stuart:
        print("Stuart", score_stuart)
    elif points_kevin > score_stuart:
        print("Kevin", points_kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = "W" * 10000
    start = time.perf_counter()
    minion_game(s)
    end = time.perf_counter()
    print(end-start)
