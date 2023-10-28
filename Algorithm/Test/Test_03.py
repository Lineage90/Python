# 1번째
# import sys

# n = int(sys.stdin.readline())

# time = []
# st_list = []

# for _ in range(n):
#     h, m, s = map(int, input().split())
#     # 문자열 합치기    
#     time.append(str(h))
#     time.append(str(m))
#     time.append(str(s))
#     st_list.append(' '.join(time))
#     time.clear()

# st_list.sort

# for i in st_list:
#     print(i)

# for i in range(len(st_list)):
#     h = int(st_list[i][0:2])
#     m = int(st_list[i][2:4])
#     s = int(st_list[i][4:6])
#     print(h,m,s)

# 2번째
import sys
n = int(sys.stdin.readline())

time = []

for _ in range(n):
    a = list(map(int, input().split()))
    time.append(a)
    
time.sort()

for i in time:
    print(' '.join(map(str, i)))