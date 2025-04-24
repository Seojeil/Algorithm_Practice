T = int(input())

for test_case in range(1, T + 1):
    l_1, l_2 = map(int, input().split())
    list_1 = list(map(int, input().split()))
    list_2 = list(map(int, input().split()))

    answer = 0

    if l_1 == l_2:
        answer = sum(a * b for a, b in zip(list_1, list_2))
    else:
        if l_2 > l_1:
            long_list, short_list, long, short = list_2, list_1, l_2, l_1
        else:
            long_list, short_list, long, short = list_1, list_2, l_1, l_2

        for n in range(long - short + 1):
            cut_list = long_list[n : n + short]
            answer = max(answer, sum(a * b for a, b in zip(cut_list, short_list)))

    print(f"#{test_case} {answer}")
