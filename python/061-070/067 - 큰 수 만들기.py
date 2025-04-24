def solution(number, k):
    stack = []

    for n in number:
        while stack and stack[-1] < n and k != 0:
            stack.pop()
            k -= 1

        stack.append(n)

    for _ in range(k):
        stack.remove(min(stack))

    answer = "".join(stack)

    return answer
