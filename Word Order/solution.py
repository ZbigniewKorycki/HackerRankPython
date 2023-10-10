num_words = int(input())

words = [input() for _ in range(num_words)]

words_with_occurrence = {}
for word in words:
    if word in words_with_occurrence:
        words_with_occurrence[word] += 1
    else:
        words_with_occurrence[word] = 1

words_values = [str(occurrence) for occurrence in words_with_occurrence.values()]

print(len(words_with_occurrence))
print(' '.join(words_values))


