# 단지번호붙이기

# 정사각형 - N
n = int(input())

# 2차배열 생성
graph = []
# 방문기록
visited = [[False]*n for _ in range(n)]
# 좌우상하
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

aptnum = 0 # 아파트 수

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    global aptnum
    visited[x][y] = True
    if graph[x][y] == 1:
        aptnum +=1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx,ny)
danji = [] # 단지별 수
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i,j)
            danji.append(aptnum)
            aptnum = 0

print(len(danji))
for n in sorted(danji):
    print(n)