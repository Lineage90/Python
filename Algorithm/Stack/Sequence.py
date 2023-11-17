import sys

input = sys.stdin.readline

n = int(input())


cnt = 0
stc = [0]
answer = []

for _ in range(n):
    m = int(input())
    while cnt < m:
        cnt += 1
        stc.append(cnt)
        answer.append('+')
        
        if cnt == m:
            stc.pop()
            answer.append('-')
    
    if cnt > m:
        if stc[-1] < m:
            stc.append(-1)
            break
        while stc[-1] >= m:
            stc.pop()
            answer.append('-')

if len(stc) != 1:
    answer = 'NO'
    print(answer)

else:
    for i in answer:
        print(i)
    
    