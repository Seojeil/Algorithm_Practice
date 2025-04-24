def solution(n):
    answer = ""

    for r in range(n):
        if r % 2 == 0:
            answer += "수"
        else:
            answer += "박"

    return answer
