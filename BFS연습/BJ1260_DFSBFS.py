from collections import deque

N,M,V = map(int,input().split())

arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited1 = [False] * (N+1)
for i in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
# 인접 리스트의 요소에 접근했을 때 BFS의 경우
#  인접 리스트 요소를 오름차 순,
#  DFS의 경우 인접 리스트 요소를 내림차 순으로
#  정렬해주어야 한다.
for i in range(1,len(arr)):
    arr[i] = sorted(arr[i])

def dfs(v):
    visited[v] = True
    print(v,end=' ')
    for i in arr[v]:
        if not visited[i]:
            dfs(i)
dfs(V)

def bfs(start):
    queue = deque([start])
    visited1[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in arr[v]:
            if not visited1[i]:
                visited1[i] = True
                queue.append(i)
print()
bfs(V)