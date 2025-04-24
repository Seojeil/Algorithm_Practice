def solution(s):
    answer = 0

    for _ in range(len(s)):
        k = s

        for _ in range(80):
            if "[]" in k:
                k = k.replace("[]", "")

            if "{}" in k:
                k = k.replace("{}", "")

            if "()" in k:
                k = k.replace("()", "")

            if k == "":
                answer += 1
                break

        s = s[1:] + s[0]

    return answer
