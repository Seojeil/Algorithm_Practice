import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(int(input()))

A.sort()

for _ in range(M):
    D = int(input())

    pos = bisect.bisect_left(A, D)

    if pos < len(A) and A[pos] == D:
        print(pos)
    else:
        print(-1)


# 직접 구현

# def bisect_left(arr, target):
#     left = 0
#     right = len(arr) - 1
#     result = -1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             result = mid
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return result
