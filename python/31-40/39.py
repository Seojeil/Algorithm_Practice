# 개인정보 수집 유효기간


def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    deadline = []
    today = int(today.replace(".", "")[:8])

    for t in terms:
        term_dict[t[0]] = int(t[2:])

    for p in privacies:
        y, m = divmod(int(p.replace(".", "")[4:6]) + term_dict[p[-1]], 12)
        if m == 0:
            m = 12
            y -= 1
        date = int(p.replace(".", "")[0:4] + "00" + p[8:10])
        deadline.append(date + m * 100 + y * 10000)

    n = 1
    for d in deadline:
        if d <= today:
            answer.append(n)
            n += 1
        else:
            n += 1

    return answer
