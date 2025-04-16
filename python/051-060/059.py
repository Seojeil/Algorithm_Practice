# 주차 요금 계산


import math


def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


def solution(fees, records):
    minute = []
    answer = []
    dict_records = {}
    records = [i.split() for i in records]

    for time, number, record in records:
        minutes = time_to_minutes(time)

        if dict_records.get(number) is None:
            dict_records[number] = -minutes
        elif record == "OUT":
            dict_records[number] += minutes
        else:
            dict_records[number] -= minutes

    key = sorted(dict_records.keys())

    for k in key:
        if dict_records[k] > 0:
            minute.append(dict_records[k])
        else:
            minute.append(dict_records[k] + 1439)

    for m in minute:
        if m <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((m - fees[0]) / fees[2]) * fees[3])

    return answer
