num_words = int(input())

words = [input() for _ in range(num_words)]

print(len(set(words)))

words_counter = []
for word in words:
    word_occurrence = words.count(word)
    words_counter.append(word_occurrence)
    words = list(filter(word.__ne__, words))

zero = 0
words_counter_without_zeros = list(filter(zero.__ne__,words_counter))

final_words = [str(n) for n in words_counter_without_zeros]

print(' '.join(final_words))

