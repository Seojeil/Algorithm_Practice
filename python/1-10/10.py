# 행렬의 덧셈


def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])

    answer = [[0] * col for i in range(row)]

    for n in range(row):
        for k in range(col):
            answer[n][k] = arr1[n][k] + arr2[n][k]

    return answer
