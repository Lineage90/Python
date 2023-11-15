# 시간 초과
# n = int(input())

# lst = []
# count = 0

# while count < n:
#     x = int(input())
#     count += 1
#     if x == 0:
#         if len(lst) == 0:
#             print(0)
#         else:
#             print(max(lst))
#             lst.remove(max(lst))
#     else:
#         lst.append(x)

# heapq 사용
import heapq
import sys

input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    a = int(input())
    if a == 0:
        if lst:
            print((-1)*heapq.heappop(lst))
        else:
            print(0)
    else:
        heapq.heappush(lst, (-1)*a)
