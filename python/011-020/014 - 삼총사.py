def solution(number):
    answer = 0

    n = len(number)

    for x in range(n):
        a = number[x]

        for y in range(x + 1, n):
            b = number[y]

            for z in range(y + 1, n):
                c = number[z]

                if a + b + c == 0:
                    answer += 1

    return answer
