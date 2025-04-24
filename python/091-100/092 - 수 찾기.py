n = int(input())

numbers_1 = set(map(int, input().split()))

m = int(input())

numbers_2 = list(map(int, input().split()))

for number in numbers_2:
    if number in numbers_1:
        print(1)
    else:
        print(0)
