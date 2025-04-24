import sys

input = sys.stdin.readline

N, M = map(int, input().split())

words = []

for _ in range(N):
    word = input()
    word = word[:-1]

    if len(word) >= M:
        words.append(word)

frequency = {}

for char in words:
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

unique_words = list(set(words))


def sort_key(word):
    return (-frequency[word], -len(word), word)


words = sorted(unique_words, key=sort_key)

for word in words:
    print(word)
