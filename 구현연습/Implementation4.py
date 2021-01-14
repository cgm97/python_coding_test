# 게임 개발
# 118 page

# 맵 크기 선언
N,M = map(int,input().split())

# 캐릭터 현재 위치 , 방향 선언
x,y,direction = map(int,input().split())
# 캐릭터 현재위치
character = [[0] * M for i in range(N)]
character[x][y] = 1
# 선언된 맵 크기만큼 생성
m = []
for i in range(N):
    m.append(list(map(int,input().split())))
# 북0 동1 남2 서3 방향 선언
dx = [-1,0,+1,0]
dy = [0,+1,0,-1]
# 게임 실행
count = 1 # 땅 밟은 횟수
turn_count = 0 # 턴 횟수

# # 왼쪽으로 회전
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

while True:
    #  turn_left()
    direction -= 1
    if direction == -1:
        direction = 3
    nx = x + dx[direction] # 캐릭터가 해당 방향으로 움직임
    ny = y + dy[direction]
    if m[nx][ny] == 0 and character[nx][ny] == 0:
        character[nx][ny] = 1 # 캐릭터가 가보지않은 방향이였지만 이제는 가본 방향으로 처리
        count+=1
        x = nx
        y = ny
        turn_count=0
        continue
    else :
        turn_count += 1
    if turn_count == 4: # 턴을 4번 다했는데 육지가 없을때
        nx = x - dx[direction] # 뒤로 빠꾸
        ny = y - dy[direction]
        if m[nx][ny] == 0: # 뒤로 빠꾸
            x = nx
            y = ny
        else : # 모든 방향이 바다이면 종료
            break
        turn_count=0
print(count)