# 단어 공부


from collections import Counter

word = input().upper()

char_dict = Counter(word)

print(char_dict)
print(max(char_dict.values()))
