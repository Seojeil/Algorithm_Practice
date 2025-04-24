def solution(price, money, count):
    total = 0

    for n in range(1, count + 1):
        total += n * price

    if total > money:
        answer = total - money
    else:
        answer = 0

    return answer
