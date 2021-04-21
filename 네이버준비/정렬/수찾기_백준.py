N_arr = []
M_arr = []

N = int(input())
N_arr = list(map(int,input().split()))
N_arr.sort()
M = int(input())
M_arr = list(map(int,input().split()))

# 시간 초과...
# for i in M_arr :
#     if i in N_arr :
#         print(1)
#     else :
#         print(0)

# 2진탐색 사용 하여 정답
def binary_sort(m, N_arr) :
    start = 0
    end = N-1
    while start <= end :
        mid = (start + end) // 2

        if m == N_arr[mid] :
            return print(1)
        elif m > N_arr[mid] :
            start = mid + 1
        else :
            end = mid - 1
    return print(0)

for m in M_arr :
    binary_sort(m,N_arr)