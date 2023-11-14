import sys
import heapq

input = sys.stdin.readline

n = int(input())

minlst = []

for _ in range(n):
    a = int(input())
    if a == 0:
        if minlst:
            print(heapq.heappop(minlst))
        else:
            print(0)
    else:
        heapq.heappush(minlst, a)