from itertools import combinations as c

t = int(input())
team = []
for _ in range(t):
    team.append(list(map(int, input().split())))

result = float("inf")

for team_1 in c(range(t), t // 2):
    team_2 = set(range(t)) - set(team_1)
    start_ab = 0
    link_ab = 0

    for s1, l1 in zip(team_1, team_2):
        for s2, l2 in zip(team_1, team_2):
            start_ab += team[s1][s2]
            link_ab += team[l1][l2]

    result = min(result, abs(start_ab - link_ab))

    if result == 0:
        break

print(result)
