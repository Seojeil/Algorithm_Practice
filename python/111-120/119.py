# 스노우볼

h, x = map(int, input().split())

MOD = 10**9 + 7

snow = []

for _ in range(h):
    snow.append(int(input()))

result = 0

while snow:
    result += snow.pop()
    result = result * x % MOD

print(result)
