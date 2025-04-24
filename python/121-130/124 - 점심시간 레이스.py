def manhattan(a, b):
    return abs(a[1] - b[1]) + abs(a[0] - b[0])


_, m, k = map(int, input().split())

classroom = {i: None for i in range(1, k + 1)}

for i in range(1, k + 1):
    classroom[i] = tuple(map(int, input().split()))

cafeteria = (1, m + 1)

for key in classroom:
    classroom[key] = manhattan(cafeteria, classroom[key])

min_value = min(classroom.values())

for key, value in classroom.items():
    if value == min_value:
        print(key)
        break
