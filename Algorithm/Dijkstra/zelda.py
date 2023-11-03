# import random
# import sys

# input = sys.stdin.readline

# n = int(input())
# count = 0
# thief = []

# for _ in range(n):
#     k = list(map(int, input().split()))
#     thief.append(k)

# start = thief[0][0]


import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

cnt = 0
# 상하좌우
dx = [-1, 1, 0, 0]    
dy = [0, 0, -1, 1]

while True:
    cnt += 1
    # 동굴 크기 입력
    n = int(input().rstrip())
    
    # 0이면 종료
    if n == 0:
        break
    
    # 이차원 리스트로 최단 경로 초기화
    dis = [[INF] * n for _ in range(n)]
    
    # 동굴 정보 입력
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    # 시작점 0, 0
    dis[0][0] = graph[0][0]
    
    q = [(graph[0][0], 0, 0)]
    
    while q:
        
        # dis = graph[x][y] 까지의 최단 경로 저장
        # x, y = 탐색 시작 지점의 좌표 저장
        road, x, y = heapq.heappop(q)
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인(상, 하, 좌, 우)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나면 탐색 종료
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            # 최단 경로를 갱신
            cost = road + graph[nx][ny]
            
            if dis[nx][ny] > cost:
                dis[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    
    # 출력
    print('Problem '+ str(cnt) + ': ' + str(dis[n-1][n-1]))