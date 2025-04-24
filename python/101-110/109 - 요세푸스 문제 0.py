import sys

N, K = map(int, sys.stdin.readline().split())

human_round = []
result = []
A = K
K -= 1

for i in range(1, N + 1):
    human_round.append(i)

while human_round:
    a = human_round.pop(K)
    result.append(a)
    if human_round:
        K = (K + A - 1) % len(human_round)

result = ", ".join(map(str, result))

print(f"<{result}>")
