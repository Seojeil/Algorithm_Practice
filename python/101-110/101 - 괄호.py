T = int(input())

for _ in range(T):
    p_s = input()

    n_p_s = []

    for p in p_s:
        if not n_p_s and p == ")":
            n_p_s.append(p)
            break
        if p == "(":
            n_p_s.append(p)
        else:
            n_p_s.pop()

    if n_p_s:
        print("NO")
    else:
        print("YES")
