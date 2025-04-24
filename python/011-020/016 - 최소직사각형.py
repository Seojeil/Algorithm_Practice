def solution(sizes):
    w = 0
    h = 0
    w_s = []
    h_s = []

    for size in sizes:
        if size[0] >= size[1]:
            w = size[0]
            h = size[1]
            w_s.append(w)
            h_s.append(h)
        else:
            w = size[1]
            h = size[0]
            w_s.append(w)
            h_s.append(h)

    answer = max(w_s) * max(h_s)

    return answer
