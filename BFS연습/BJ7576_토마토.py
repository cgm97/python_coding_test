from collections import deque

M,N = map(int,input().split())

arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    arr.append(list(map(int,input().split())))

queue = deque()
def bfs():
    while queue:
        x,y = queue.popleft() # 제일 앞칸 2개 꺼내기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M: # 배열 범위 안이면
                if arr[nx][ny] == 0: # 해당 배열값이 익지않은 토마토면
                    arr[nx][ny] = arr[x][y] + 1 # 일수 증가
                    queue.append((nx,ny)) # 해당 값 다시 넣기

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i,j))# 익은 토마토가 어디있는지 확인 후 저장

result = -1
condition = 1

bfs() # 실행

for i in arr:
    for j in i:
        if j == 0: # 0이 하나라도있으면 익지않은 토마토 존재
            condition = 0
        result = max(result,j) # 가장 높은것이 걸리는 일수
if condition == 0:
    print(-1) # 모두 익지않음
elif result == 1:
    print(0) # 그대로
else:
    print(result-1) # 2일차 부터 시작되므로 -1 