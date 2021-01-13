# 왕실의 나이트
# 115page

# 말이 움직일수있는 방향 최대 8가지
# 입력 ex) a1 , b2
key = input()
row = int(ord(key[0]))-ord('a')+1 # a=1 , b=2 ...
col = int(key[1])

# 말의 움직임 - 최대 8가지 방법
step = [(-2,-1),(-1,-2),(+1,-2),(+2,-1),(+2,+1),(+1,+2),(-1,+2),(-2,+1)]
result = 0
for start in step:
    movingR = row + start[0]
    movingC = col + start[1]
    if movingR>0 and movingR<9 and movingC>0 and movingC<9:
        result+=1
print(result)

##### 복습 #####
input_data = list(input())

row = int(ord(input_data[0])) - int(ord('a')) + 1
col = int(input_data[1])

step = [(-2,-1),(-1,-2),(+1,-2),(+2,-1),(+2,+1),(+1,+2),(-1,+2),(-2,+1)]

count=0

for steps in step :
    x = row + steps[0]
    y = col + steps[1]

    if x > 0 and y > 0 and x < 9 and y < 9 :
        count+=1
print(count)