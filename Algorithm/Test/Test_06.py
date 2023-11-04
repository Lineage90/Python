# import sys
# import itertools

# input = sys.stdin.readline

# def count_paths(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2

#     # n = 1, 2인 경우는 미리 계산하였으므로 3부터 시작
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 2

#     for i in range(3, n + 1):
#         # 경로 수 합치기
#         dp[i] = dp[i - 1] + dp[i - 2]

#     return dp[n]

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     result = count_paths(n)
#     print(result)
    
# 흠

import sys
import itertools

input = sys.stdin.readline

def count_road(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    road = []
    road.append(1)
    road.append(2)
    
    for i in range(2, n):
        road.append(road[i - 2] + road[i - 1])
    
    return road[n-1]


while True:
    n = int(input())
    if n == 0:
        break
    result = count_road(n)
    print(result)
    