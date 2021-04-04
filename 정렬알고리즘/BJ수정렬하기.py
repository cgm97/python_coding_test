# N개의 수가 주어 졌을 경우 이를 오름차순으로 정렬 하는
# 프로그램 작성

N = int(input())
arr = []
for i in range(N) :
    arr.append(int(input()))

arr.sort()
for j in range(len(arr)) :
    print(arr[j])
    