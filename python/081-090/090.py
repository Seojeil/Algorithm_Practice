# 등수 구하기


N, t, P = map(int, input().split())

if N != 0:
    ranking = list(map(int, input().split()))
    ranking.sort(reverse=True)
    sort_ranking = ranking[:]
    sort_ranking.append(t)
    sort_ranking.sort(reverse=True)
    sort_ranking = sort_ranking[:P]

    if sort_ranking == ranking or t not in sort_ranking:
        print(-1)
    else:
        for i in range(P):
            if sort_ranking[i] == t:
                print(i + 1)
                break
else:
    print(1)
