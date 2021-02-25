# 삽입 정렬
# 시간 복잡고 O(N제곱) 하지만 리스트의 데이터가 거의 정렬되어있으면 매우 빠르게 정렬 된다.
# 선택 정렬과 흡사한 시간이 소요

arr = [7,4,6,1,2,10]

for i in range(len(arr)) :
    for j in range(i,0,-1) :
        if arr[j] < arr[j-1] :
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else :
            break

print(arr)