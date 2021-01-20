# 유기농 배추

import sys
sys.setrecursionlimit(10**8)

test = int(input()) # 테스트 횟수

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = [] # 테스트 케이스 만큼 결과 저장
def dfs(x,y,count):
    arr[x][y] = 0 # 방문 했으므로 0 초기화
    for i in range(4): # 4방향 체크
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                dfs(nx,ny,count)

for _ in range(test): # 테스트 개수 반복
    m,n,k = map(int,input().split()) # 가로 , 세로 , 마리수
    arr = [[0]*m for _ in range(n)] # 입력된 배열 생성

    for _ in range(k): # 배추 설정
        i,j = map(int,input().split())
        arr[j][i] = 1

    count = 0 # 배추 흰지렁이 수

    for i in range(n): # 세로 - DFS 탐색
        for j in range(m): # 가로
            if arr[i][j] == 1:
                count += 1
                dfs(i,j,count)
    result.append(count)

for i in result:
    print(i)
