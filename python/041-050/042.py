# 신고 결과 받기


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    accused = {e: [] for e in id_list}
    mail = {e: 0 for e in id_list}

    for r in report:
        r = r.split(" ")
        accused[r[1]].append(r[0])

    for a in accused:
        if len(accused[a]) >= k:
            for n in accused[a]:
                mail[n] += 1

    for n in mail:
        answer.append(mail[n])

    return answer
