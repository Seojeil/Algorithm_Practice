# 수도 요금 경쟁


T = int(input())

for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())

    a = p * w

    additional = 0
    if w > r:
        additional = (w - r) * s
    b = q + additional

    print(f"#{test_case} {min(a, b)}")
