# DFS 알고리즘
# 142 page

# # 함수 생성 - DFS 알고리즘 - 재귀함수
# def dfs(graph,v,visited):
#     # 현재 노드 방문 기록 저정
#     visited[v] = True
#     print(v)
#     # grape 노드 중 방문 하지 않은 노드 간선 일때까지 반복
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)
# # 그래프 설정
# graph = [
#     [],# 1번부터 8번까지 만들기 위해 0번지는 생략
#     [2,3,8], # 1번 노드와 이어진 간선들
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7] # 8번 노드와 이어진 간선들
# ]

# # 노드 방문 기록
# visited = [False] * 9
# print(visited)

# dfs(graph,1,visited)

# 다시 풀어보기

# DFS 알고리즘 - 깊이 우선 탐색 - 스택 사용
def dfs(graph,v,visited):
    # 방문 기록 체크
    visited[v] = True
    print(v,end=' ')
    # graph 노드 반복 하여 연결된 간선 체크
    for i in graph[v]:
        # 만약 방문한적 없는 노드 일 경우
        if not visited[i]:
            dfs(graph,i,visited)

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
# 방문 기록 체크 하는 배열 생성
visited = [False] * 9

dfs(graph,1,visited) # 1부터 시작