from itertools import combinations

N = int(input())
population = list(map(int, input().split()))
all_pop = sum(population)

zone = {key: [] for key in range(1, N + 1)}

for i in range(1, N + 1):
    zone[i] = list(map(int, input().split()))[1:]


def is_connect(z):
    if len(z) == 1:
        return True

    z = list(z)
    connect = [z[0]]

    for constituency in connect:
        for node in zone[constituency]:
            if node in z and node not in connect:
                connect.append(node)

    return len(z) == len(connect)


my_zone = []
another_zone = []

for i in range(1, N):
    for comb in combinations(range(1, N + 1), i):
        comb = set(comb)
        my_zone.append(comb)
        another_zone.append(set(range(1, N + 1)) - comb)

explore = []
divided_zone = []

for m, a in zip(my_zone, another_zone):
    if m not in explore and a not in explore:
        explore.append(m)
        explore.append(a)

        if is_connect(m) and is_connect(a):
            divided_zone.append(list(m))

if divided_zone:
    result = float("inf")

    for z in divided_zone:
        cur_pop = 0
        for my_pop in z:
            cur_pop += population[my_pop - 1]
        result = min(result, abs(all_pop - cur_pop * 2))
else:
    result = -1

print(result)
