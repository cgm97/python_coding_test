import math
X,Y = map(int,input().split())

Z = math.floor(100 * Y/X)

# 시간 초과... - 수정전
# if Z >= 99 :
#     print(-1)
# else :
#     count = 0
#     while True:
#         if math.floor(100*((Y+count)/(X+count))) > Z :
#             break
#         else :
#             count += 1
#     print(count)

# 이진탐색... - 수정후
start, end = 1,1000000000
if Z >= 99 :
    print(-1)
else :
    count = 0
    while start <= end :
        mid = (start+end) // 2
        total, win = X+mid, Y+mid
        if math.floor(100*win/total) > Z :
            end = mid - 1
            count = mid
        else :
            start = mid + 1
    print(count)