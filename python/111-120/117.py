# 파이프 옮기기 1


from collections import deque

t = int(input())

house = []

for _ in range(t):
    house.append(list(map(int, input().split())))

x = 1
y = 0


def move(x, y, t):
    dp = [[[0] * 3 for _ in range(t)] for _ in range(t)]
    dp[y][x][0] = 1

    for y in range(t):
        for x in range(t):
            if house[y][x] == 1:
                continue

            if x + 1 < t and house[y][x + 1] == 0:
                dp[y][x + 1][0] += dp[y][x][0] + dp[y][x][2]
            if y + 1 < t and house[y + 1][x] == 0:
                dp[y + 1][x][1] += dp[y][x][1] + dp[y][x][2]
            if (
                y + 1 < t
                and x + 1 < t
                and house[y][x + 1] == 0
                and house[y + 1][x] == 0
                and house[y + 1][x + 1] == 0
            ):
                dp[y + 1][x + 1][2] += dp[y][x][0] + dp[y][x][1] + dp[y][x][2]

    return dp[t - 1][t - 1][0] + dp[t - 1][t - 1][1] + dp[t - 1][t - 1][2]


print(move(x, y, t))
