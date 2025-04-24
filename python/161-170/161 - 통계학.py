import sys

input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers.sort()


def find_mode(numbers):
    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_frequency = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_frequency]

    return modes


# 산술평균
print(round(sum(numbers) / N))

# 중앙값
print(numbers[N//2])

# 최빈값
mode = find_mode(numbers)

if len(mode) == 1:
    print(mode[0])
else:
    print(mode[1])

# 범위
print(max(numbers) - min(numbers))
