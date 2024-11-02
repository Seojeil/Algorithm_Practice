# 행렬의 곱셈


def solution(arr1, arr2):
    row1 = len(arr1)
    col1 = len(arr1[0])

    row2 = len(arr2)
    col2 = len(arr2[0])

    answer = [[0 for x in range(col2)] for x in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for n in range(col1):
                answer[i][j] += arr1[i][n] * arr2[n][j]

    return answer
