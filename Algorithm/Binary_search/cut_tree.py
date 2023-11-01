# 이진 탐색 - 2200ms
import sys

input= sys.stdin.readline

def binary_search(arr, start, end):
    res = 0
    while start <= end:
        # 중간값
        mid = (start+end) // 2
        chainsaw = 0
        
        for x in arr:
            if x > mid:
                chainsaw += x- mid
        # 나무 부족 -> 높이 down    
        if chainsaw < m:
            end = mid-1
        # 나무 충분 -> 높이 up
        else:
            res = mid
            start = mid +1
    return res
        
# 입력
n , m = map(int,input().split())
# 출력
trees = list(map(int,input().split()))

# 함수 호출
r = binary_search(trees, 0, max(trees))

print(r)

# 매개 변수 탐색 - 4740ms
# from sys import stdin

# input = stdin.readline

# N,M = map(int, input().split())

# tree = list(map(int, input().split()))

# start, end = 1, max(tree)

# while start <= end:
#     mid = (start + end) // 2
#     tree_len = 0
#     # 나무 자르기
#     for i in tree:
#         if mid <= i:
#             tree_len += i-mid

#     # 나무 충분, 높이 up
#     if tree_len >= M:
#         start = mid + 1
    
#     # 나무 부족, 높이 down
#     else:
#         end = mid - 1
        
# print(end)


