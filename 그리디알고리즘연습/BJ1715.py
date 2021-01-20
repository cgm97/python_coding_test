# 그리디 알고리즘
# 카드정렬

# N = int(input()) # 카드 묶음수
# arr = []
# for _ in range(N):
#     arr.append(int(input()))
# arr.sort() # 오름차순 정렬
# sum = 0
# for i in range(len(arr)-1):
#     sum = sum + arr[i] + arr[i+1]
#     arr[i+1] = sum
# print(sum)

import heapq
N = int(input()) # 카드 묶음수
arr = []
for _ in range(N):
    heapq.heappush(arr,int(input()))
if len(arr) == 1:
    print(0)
else:
    sum = 0
    while len(arr) >1:
        item1 = heapq.heappop(arr)
        item2 = heapq.heappop(arr)
        sum += item1 + item2
        heapq.heappush(arr,item2+item1)
    print(sum)