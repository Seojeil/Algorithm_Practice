# 피로도


from itertools import permutations as p


def solution(k, dungeons):
    answer = 0
    number_dungeon = len(dungeons)
    for dungeon in p(range(number_dungeon)):
        current_k = k
        for i, d in enumerate(dungeon):
            if current_k < dungeons[d][0]:
                answer = max(answer, i)
                break
            current_k -= dungeons[d][1]
        else:
            return number_dungeon

    return answer
