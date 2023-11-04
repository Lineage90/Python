# itertools 사용
import sys
import itertools

t = int(sys.stdin.readline())

for i in range(1,t+1):
    l = list(input())
    print(f'Case # {i}:')
    per = list(itertools.permutations(l))
    for j in per:
        print(''.join(j))


