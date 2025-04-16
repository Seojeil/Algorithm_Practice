# 연속된 부분 수열의 합


from collections import deque


def solution(sequence, k):
    start = 0
    end = -1
    sub_seq = deque()
    sum_sub_seq = 0
    current_len = float("inf")

    for seq in sequence:
        while sum_sub_seq + seq > k and sub_seq:
            sum_sub_seq -= sub_seq[0]
            sub_seq.popleft()
            start += 1
        sum_sub_seq += seq
        sub_seq.append(seq)
        end += 1
        if sum_sub_seq == k:
            if (end - start) < current_len:
                current_len = end - start
                min_start = start
                min_end = end

    return [min_start, min_end]
