# 택배 상자


from collections import deque


def solution(order):
    answer = 0
    main_container = deque(range(1, len(order) + 1))
    sub_container = deque()

    for o in order:
        while True:
            if main_container and not sub_container:
                if o == main_container[0]:
                    main_container.popleft()
                    answer += 1
                    break
                else:
                    sub_container.appendleft(main_container[0])
                    main_container.popleft()

            elif main_container and sub_container:
                if o == main_container[0]:
                    main_container.popleft()
                    answer += 1
                    break
                elif o == sub_container[0]:
                    sub_container.popleft()
                    answer += 1
                    break
                else:
                    sub_container.appendleft(main_container[0])
                    main_container.popleft()

            elif not main_container and sub_container:
                if o == sub_container[0]:
                    sub_container.popleft()
                    answer += 1
                    break
                else:
                    return answer

    return answer
