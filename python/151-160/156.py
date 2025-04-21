# 그룹 단어 체커


N = int(input())

result = N

for _ in range(N):
    word = list(input())

    while len(word) >= 2:
        alpha = word.pop(0)
        while word and word[0] == alpha:
            word.pop(0)
        if alpha in word:
            result -= 1
            break

print(result)
