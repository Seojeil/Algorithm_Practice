import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

a = 0
b = 0

for A_card, B_card in zip(A, B):
    if A_card > B_card:
        a += 1
    elif B_card > A_card:
        b += 1

if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("D")
