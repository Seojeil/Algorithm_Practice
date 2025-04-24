def count(string):
    result = {}

    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    return result


def solution(X, Y):
    answer = ""
    count_X = count(X)
    count_Y = count(Y)

    for i in "9876543210":
        if i in count_X:
            if i in count_Y:
                answer += str(i * min(count_X[i], count_Y[i]))

    if answer == "":
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"

    return answer
