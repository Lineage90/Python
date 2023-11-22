import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())

# deque로 만들어준다
deq = deque([i for i in range(1, n+1)])

index = list(map(int, input().split()))

count = 0

for num in index:
    while 1:
        if deq[0] == num:
            deq.popleft()
            break
        
        else:
            if deq.index(num) <= len(deq)//2:
                deq.rotate(-1)
                count += 1
            else:
                deq.rotate(1)
                count += 1
print(count)
