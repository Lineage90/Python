import sys

n = int(sys.stdin.readline())
srt = []

for i in range(n):
    nums = int(sys.stdin.readline())
    srt.append(nums)

srt.sort()

for i in srt:
    print(i)