# 선택 알고리즘
# O(n제곱)의 효율

# 배열 0 번지 부터 끝까지 검색하여 0번지의 값보다 작은값이 존재하면 
# 해당되는 i번지의 위치값을 0번지 값과 스위칭 i+1씩 증가하여 배열 끝까지 검색

arr = [7,4,6,1,2,10]

for i in range(len(arr)) :
    min_value = i # arr 위치 저장
    for j in range(i+1,len(arr)) : 
        if arr[min_value] > arr[j] :
            min_value = j # arr 작은 값 위치 저장
    arr[i], arr[min_value] = arr[min_value], arr[i]

print(arr)