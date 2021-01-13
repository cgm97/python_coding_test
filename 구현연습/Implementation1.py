# 상하좌우 - 구현
# 110 page

# N * N 크기 정사각형 생성
n = int(input())
# 이동 계획서 입력 (L R U D)
move = input().split()
# 초기 위치 지정
x , y = 1,1

mx = [0,0,-1,+1] # 왼 오 상 하 이동시 2차원배열
my = [-1,+1,0,0] # 왼 오 상 하 이동시 2차원배열
moveType = ['L','R','U','D']

# 구현
for move_c in move:
    for i in range(len(moveType)):
        if move_c == moveType[i]:
            cx = x + mx[i]
            cy = y + my[i]
    if cx == 0 or cy == 0 or n < cx or n < cy :
        continue
    x,y = cx,cy
print(x,y)



# 복습 - 다른 버젼으로 작성해봄
n = int(input())
data = list(input().split())

x,y = 0,0
moveType=['동','서','남','북']
mx = [0,0,+1,-1]
my = [+1,-1,0,0]

for move in data: # 입력된 동서남북 판별
    for i in range(len(moveType)): # 동서남북 계산
        if move == moveType[i]: # 각각의 동서남북 계산 후 현재위치로 선정
            cx = x + mx[i]
            cy = y + my[i]
    if cx == -1 or cy == -1 or cx > n or cy > n: # 계획서 범위벗어나면 큰일남
        continue
    x,y = cx,cy # 벗어나지 않으면 현재위치로 선정
# 출력
print(x,y)