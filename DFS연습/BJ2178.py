# 미로탐색

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# DFS
def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny]==1 and visit[nx][ny]==0:
                arr[nx][ny] = arr[x][y]+1 # 방문처리
                visit[nx][ny] = 1

                dfs(nx,ny)

N,M = map(int,input().split())
visit = [[0]*M for _ in range(N)]
arr = []
for _ in range(N): # 배열 생성
    arr.append(list(map(int,input())))
count = 0
dfs(0,0)
print(arr[N-1][M-1])