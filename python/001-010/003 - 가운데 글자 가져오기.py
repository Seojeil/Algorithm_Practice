def solution(s):
    answer = ""

    if len(s) % 2 == 0:
        k = len(s) // 2
        answer = s[k-1 : k+1]
    else:
        k = len(s) // 2
        answer = s[k]

    return answer
