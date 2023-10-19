# 카드 2
import collections

N = int(input())
card = collections.deque()

for i in range(N):
    card.append(i+1)

for j in range(N-1):
    card.popleft()
    card.append(card[0])
    card.popleft()
    
print(card[0])