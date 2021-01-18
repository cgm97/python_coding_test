# 컴퓨터 수
com_count = int(input())
# 네트워크망 수
network_count = int(input())
visited = [False]*(com_count+1)

# graph = [
#     [],
#     [[1,2],
#     [2,3],
#     [1,5],
#     [5,2],
#     [5,6],
#     [4,7]]
# ]
graph = [[] for _ in range(com_count+1)]

for i in range(network_count):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)
print(visited.count(True)-1)