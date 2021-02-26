# N개의 수가 주어 졌을 경우 이를 오름차순으로 정렬 하는
# 프로그램 작성
# O nlogn 

import sys
sys.setrecursionlimit(10**4)

N = int(input())
arr = []
for _ in range(N) :
    arr.append(int(input()))

for i in sorted(arr) :
    print(i)

# def quick(arr,start,end) :
#     if start >= end :
#         return
#     pibot = start
#     left = start + 1
#     right = end

#     while left <= right : 
#         while left <= end and arr[left] <= arr[pibot] : # 큰값 찾을때 까지
#             left += 1
#         while right > start and arr[right] >= arr[pibot] : # 작은값 찾을때 까지
#             right -= 1
#         if left >= right :
#             arr[pibot], arr[right] = arr[right], arr[pibot]
#         else :
#             arr[left],arr[right] = arr[right], arr[left]
    
#     quick(arr,start,right-1)
#     quick(arr,right+1,end)
# quick(arr,0,len(arr)-1)

# for i in arr :
#     print(i)
