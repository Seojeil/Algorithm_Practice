import sys

input = sys.stdin.readline

N = int(input())

result = 0
room = set()

for _ in range(N):
    user = input()

    if user == 'ENTER\n':
        result += len(room)
        room = set()
    else:
        room.add(user)

result += len(room)

print(result)
