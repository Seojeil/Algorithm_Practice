# 크로아티아 알파벳


word = list(input())
result = 0

CROATIA = {
    'c': ['c=', 'c-'],
    'd': ['dz=', 'd-'],
    'l': ['lj'],
    'n': ['nj'],
    's': ['s='],
    'z': ['z=']
    }

while word:
    w = word.pop(0)

    if w in CROATIA.keys() and len(word) >= 1:
        w0 = word[0]

        if w + w0 in CROATIA[w]:
            word.pop(0)

        if w == 'd' and len(word) >= 2 and w + w0 + word[1] == 'dz=':
            word = word[2:]

    result += 1

print(result)
