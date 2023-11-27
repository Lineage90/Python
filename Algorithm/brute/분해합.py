import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == n:
        print(i)
        break
    if i == n:
        print(0)