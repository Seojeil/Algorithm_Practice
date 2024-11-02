# 성격 유형 검사하기


def solution(survey, choices):
    INDEX = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    answer = ""

    for s in range(len(survey)):
        if choices[s] > 4:
            INDEX[survey[s][1]] += choices[s] - 4
        elif choices[s] < 4:
            INDEX[survey[s][0]] -= choices[s] - 4

    if INDEX["R"] >= INDEX["T"]:
        answer += "R"
    else:
        answer += "T"

    if INDEX["C"] >= INDEX["F"]:
        answer += "C"
    else:
        answer += "F"

    if INDEX["J"] >= INDEX["M"]:
        answer += "J"
    else:
        answer += "M"

    if INDEX["A"] >= INDEX["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer
