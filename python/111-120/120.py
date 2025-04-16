# 교수님 그림이 깨지는데요?


n, k = map(int, input().split())

image = []

for _ in range(n):
    image.append(list(map(int, input().split())))

up_image = [[] for _ in range(n * k)]

for i in range(n * k):
    for j in range(n * k):
        up_image[i].append(image[i // k][j // k])

for i in up_image:
    print(" ".join(map(str, i)))
