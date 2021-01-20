# 147 page
# BFS - 넓이 우선 탐색
from collections import deque

def bfs(graph,start,visited):
    queue = deque([start]) # deque 라이브러리 사용
    visited[start] = True # 방문 처리
    while queue: # queuerk 비워질 때 까지 
        v = queue.popleft() # 가장 먼저 넣어진 큐 꺼내기
        print(v,end=' ') # 꺼내진 큐 출력
        for i in graph[v]: # 해당 노드와 연결되고, 방문하지않은 노드 큐에 삽입
            if not visited[i]:
                visited[i] = True # 방문처리
                queue.append(i) # 삽입

visited = [False]*9
# Graph 생성
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
bfs(graph,1,visited)