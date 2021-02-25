# 퀵 정렬
# 시간 복잡도 O(Nlong N)
# 다른 정렬에 비해 매우 빠르고 가장 많이 쓰임
# 배열을 반으로 쪼개 검사
# 초기 피봇 - arr[0]
# 반으로 쪼갠 기준으로 왼쪽은 초기 피봇 + 1 부터 오른쪽은arr[] 가장 뒤부분 순으로 검사
# 쪼갠 뒤 왼쪽은 현재 피봇보다 큰수를 찾고, 오른쪽은 현재 피봇보다 작은 수를 찾는다.
# 찾은 큰수는 오른쪽으로 보내고, 작은수는 왼쪽으로 스위칭
# 이런식으로 분할이 되었다면 왼쪽과 오른쪽 각각 정렬 하여 결과값 도출

arr = [5,7,9,0,3,1,6,2,4]

def sort(arr,start,end) : # 이해 한 뒤 나의 풀이
    if start >= end :
        return # 모두 처리 완료 간주
    pibot = start # 기준점 - arr[start]
    left = start + 1 # 기준점으로 부터 오른쪽으로 검사
    right = end # 끝에서 부터 왼쪽으로 검사

    while left <= right :
        while left <= end and arr[left] <= arr[pibot] : # 왼쪽은 기준점 보다 큰값을 찾을때까지 반복
            left += 1
        while right > start and arr[right] >= arr[pibot] : # 오른쪽은 기준점 보다 작은 값을 찾을때까지 반복
            right -= 1
        if left >= right : # 만약 검색 도중 left 와 right 값이 서로 겹치거나 지나 쳤을경우
            arr[pibot], arr[right] = arr[right], arr[pibot] # 기준점보다 작은 right값을 기준값(pibot)과 스위칭
        else : # 정상적으로 찾을 경우
            arr[left], arr[right] = arr[right], arr[left] # 왼쪽에서 찾은 큰값, 오른쪽에서 찾은 작은값을 스위칭
    
    # sort(arr,start,left-1)
    # sort(arr,left+1,end)
    sort(arr,start,right-1)
    sort(arr,right+1,end)

sort(arr,0,len(arr)-1)
print(arr)

# 책 풀이
def quick_sort(arr,start,end) :
    if start >= end : #start는 0번지부터 시작 end는 끝번지부터 시작 하여 start와end가 같거나 start가 큰값이면 정렬이 끝났다고 간주
        return
    pivot = start # 초기 피봇 arr[0]
    left = start + 1 # pivot + 1\
    right = end

    while left <= right: # 왼쪽이 오른쪽 위치보다 커지면 위치값이 반 이상 이므로 종료
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
            print("arr-left",left)
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
            print("arr-right",right)
        if left >= right :
            arr[right], arr[pivot] = arr[pivot], arr[right]
            print(">=",arr)
        else :
            arr[left],arr[right] = arr[right],arr[left]
            print("left",left,"right",right)
            print("correct",arr)
        
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)

quick_sort(arr,0,len(arr)-1)
print(arr)    		