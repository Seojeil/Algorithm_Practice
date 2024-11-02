# 준환이의 운동관리

T = int(input())

for test_case in range(1, T + 1):
    l, u, x = map(int, input().split())

    if x < l:
        result = l - x
    elif x > u:
        result = -1
    else:
        result = 0

    print(f"#{test_case} {result}")
