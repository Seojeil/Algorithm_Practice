# 바이러스

n = int(input())
computers = {i: [] for i in range(1, n + 1)}

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)


def bfs(graph, n):
    infection = []
    computer = 1
    infection.append(computer)
    count = 0

    for i in infection:
        if count >= n:
            break

        while graph[i]:
            if graph[i][0] not in infection:
                k = graph[i].pop(0)
                infection.append(k)
                count += 1
            else:
                graph[i].pop(0)

    return count


print(bfs(computers, n))
