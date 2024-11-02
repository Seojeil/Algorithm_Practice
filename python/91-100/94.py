# 별 찍기

N = int(input())

for n in range(2 * N - 1):
    k = abs(n - N + 1)

    star = k * " " + "*" + "*" * ((N - k - 1) * 2)

    print(star)
