# 음료수 얼려먹기
# 149page

N,M = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

arr = []

for i in range(N):
    arr.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >=N or y <= -1 or y >=M:
        return False
    if arr[x][y] == 0 :
        for i in range(4):
            arr[x][y] = 1
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False
count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1
print(count)