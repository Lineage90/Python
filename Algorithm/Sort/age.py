
import sys
n = int(sys.stdin.readline())

user = []

for _ in range(n):
    a = list(map(str, input().split()))
    user.append(a)

user.sort(key=lambda age: int(age[0]))

for i in user:
    print(i[0], i[1])
    