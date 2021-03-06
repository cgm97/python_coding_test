# 152 page

from collections import deque

N,M = map(int,input().split())
arr = []

for i in range(N):
    arr.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >=M:
                continue
            # 미로가 벽이면 무시
            if arr[nx][ny] == 0:
                continue
            # 미로가 길이면 최단거리 계산
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y]+1
                queue.append((nx,ny))
    return arr[N-1][M-1]
print(bfs(0,0))