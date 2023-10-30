import sys

n = int(sys.stdin.readline())
alpha = []


for _ in range(n):
    alp = input()
    alpha.append(alp)
    
alpha.sort()
print(alpha)