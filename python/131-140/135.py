# 어디에 단어가 들어갈 수 있을까

T = int(input())


def check(arr, l, word):
    answer = 0

    for row in range(l):
        arr[row].append(0)
        word_space = [0]

        for col in range(l):
            if word_space and arr[row][col] == 1 and word_space[0] == 0:
                word_space.append(1)
                if sum(word_space) == word:
                    if arr[row][col + 1] == 0:
                        answer += 1
                    word_space = []
            else:
                word_space = []
                if arr[row][col] == 0:
                    word_space.append(0)
    return answer


for test_case in range(1, T + 1):
    l, word = map(int, input().split())
    puzzle = []
    for _ in range(l):
        numbers = list(map(int, input().split()))
        puzzle.append(numbers)

    transposed_puzzle = [[0] * l for _ in range(l)]

    for i in range(l):
        for j in range(l):
            transposed_puzzle[j][i] = puzzle[i][j]

    result = check(puzzle, l, word) + check(transposed_puzzle, l, word)

    print(f"#{test_case} {result}")
