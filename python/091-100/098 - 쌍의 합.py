import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    n_list = []

    for i in range(1, (n + 1) // 2):
        if i != n - i:
            n_list.append((i, n - i))

    output = ", ".join(" ".join(map(str, t)) for t in n_list)

    print(f"Pairs for {n}: {output}")
