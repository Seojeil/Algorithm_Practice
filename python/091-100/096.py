# 단지번호붙이기

N = int(input())

apartment = []

result = []
count = 0


def bfs(i, j):
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, -1, 1]
    explore = []
    explore.append((i, j))
    apartment[i][j] = 0
    answer = 1

    while explore:
        y, x = explore.pop(0)
        for d in range(4):
            dx = x + delta_x[d]
            dy = y + delta_y[d]
            if 0 <= dx < N and 0 <= dy < N and apartment[dy][dx] == 1:
                explore.append((dy, dx))
                apartment[dy][dx] = 0
                answer += 1

    return answer


for _ in range(N):
    answer = 0
    apartment.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        if apartment[i][j] == 1:
            count += 1
            result.append(bfs(i, j))

print(count)
result.sort()

for r in result:
    print(r)
