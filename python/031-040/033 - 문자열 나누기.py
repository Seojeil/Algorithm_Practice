def solution(s):
    answer = 0

    while s:
        word = s[0]
        count = 0
        len_word = 0

        for char in s:
            if char == word:
                count += 1
            else:
                count -= 1

            len_word += 1

            if count == 0:
                s = s[len_word:]
                answer += 1
                break

            if len_word >= len(s):
                s = None
                answer += 1
                break

    return answer


s = "abracadabra"

print(solution(s))
