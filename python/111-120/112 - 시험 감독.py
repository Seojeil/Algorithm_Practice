N = int(input())

A = list(map(int, input().split()))

B, C = map(int, input().split())

result = 0

for a in A:
    a -= B
    result += 1
    if a > 0:
        if a % C == 0:
            result += a // C
        else:
            result += (a // C) + 1

print(result)
