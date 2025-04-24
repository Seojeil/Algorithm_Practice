word = input()

result = 1

for n in range(len(word) // 2):
    if word[n] != word[-(n + 1)]:
        result = 0
        break

print(result)
