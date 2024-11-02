# 타슈

_ = int(input())

difference = 0

storage_a = list(map(int, input().split()))
storage_b = list(map(int, input().split()))

for a, b in zip(storage_a, storage_b):
    difference += abs(a - b)

print(difference // 2)
