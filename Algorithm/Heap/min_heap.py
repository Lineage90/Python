import sys
import heapq

n = int(input())

minlst = []

for _ in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if minlst:
            print(heapq.heappop(minlst))
        else:
            print(0)
    else:
        heapq.heappush(minlst, a)