def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)

    if total_sum % 2 != 0:
        return -1

    answer = 0
    target_sum = total_sum // 2
    combined_queue = queue1 + queue2 + queue1
    len_queue = len(queue1)

    left = 0
    right = len_queue - 1
    current_sum = sum(queue1)

    while right < len_queue * 2 - 1:
        if current_sum == target_sum:
            return answer
        elif current_sum < target_sum:
            right += 1
            if right < len_queue * 2:
                current_sum += combined_queue[right]
                answer += 1
        elif current_sum > target_sum:
            current_sum -= combined_queue[left]
            left += 1
            answer += 1

    return -1
