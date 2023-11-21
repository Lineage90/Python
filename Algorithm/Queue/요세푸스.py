import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

# deque 생성
deq = deque([i for i in range(1, n+1)])

# 요세푸스 생성
result = []

while len(deq) != 0:
    for _ in range(k-1):
        deq.append(deq.popleft())
    
    result.append(str(deq.popleft()))

print('<'+', '.join(result)+'>')