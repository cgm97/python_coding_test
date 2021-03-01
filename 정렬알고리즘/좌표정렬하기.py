#  2차원 평면 위의 점 N개가 주어진다.
#  좌표를 x좌표가 증가하는 순으로, 
#  x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 
#  다음 출력하는 프로그램을 작성하시오.

N = (int(input()))

arr = []
for _ in range(N) : 
    arr.append(list(map(int,input().split())))

# for i in range(N-1) :
#     for j in range(N-1) :
#         if arr[i][0]>arr[i+1][0] :
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#         if arr[0][i] > arr[0][i+1] :
#             arr[i],arr[i+1] = arr[i+1],arr[i]
sortArr = sorted(arr)
for i in range(N) :
    print(sortArr[i][0], sortArr[i][1])

#  2차원 평면 위의 점 N개가 주어진다.
#  좌표를 x좌표가 증가하는 순으로, 
#  y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 
#  다음 출력하는 프로그램을 작성하시오.

N = (int(input()))

arr = []
for _ in range(N) : 
    [x,y] = list(map(int,input().split()))
    ready = [y,x]
    arr.append(ready)

# for i in range(N-1) :
#     for j in range(N-1) :
#         if arr[i][0]>arr[i+1][0] :
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#         if arr[0][i] > arr[0][i+1] :
#             arr[i],arr[i+1] = arr[i+1],arr[i]
sortArr = sorted(arr)
for i in range(N) :
    print(sortArr[i][1], sortArr[i][0])
    

    
