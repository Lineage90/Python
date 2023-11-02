import heapq

def dijkstra(graph, start):
    # start로 부터의 거리를 저장
    distances = {node: float('inf') for node in graph}
    # 시작값은 0이여야 함
    distances[start] = 0
    queue = []
    # 시작 노드부터 탐색
    heapq.heappush(queue, [distances[start], start])
    
    while queue: # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue) # 탐색 할 노드, 거리를 가져온다
        
        if distances[current_destination] < current_distance: # 기존 거리보다 길다면 통과
            continue
        
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]: # 알고있는 거리보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination]) # 다음 인접 거리를 계산하기 위해 큐에 삽입
    
    return distances

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(graph, 'A'))