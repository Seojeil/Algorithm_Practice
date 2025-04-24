def solution(k, score):
    a = []
    answer = []
    for s in score:
        a.append(s)
        a.sort(reverse=True)
        try:
            a = a[:k]
        except:
            if len(a) > k:
                b = a
        answer.append(min(a))
    return answer
