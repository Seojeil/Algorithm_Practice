# 기능개발


def solution(progresses, speeds):
    answer = []

    while progresses:
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        n = 0
        while progresses[0] >= 100:
            n += 1

            if len(progresses) == 1:
                if progresses[0] >= 100:
                    progresses = []
                    break
                else:
                    answer.append(n)
                    n = 1
                    progresses = []
                    break
            progresses = progresses[1:]
            speeds = speeds[1:]
        answer.append(n)

    return answer
