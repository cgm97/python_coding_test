N,M = map(int,input().split())
tree = list(map(int,input().split()))

# 시간초과
# H = 0
# while True :
#     result = 0
#     for i in range(N) :
#         if tree[i] > H :
#             result += tree[i] - H
#     if result <= M :
#         break
#     else :
#         H += 1
# print(H)

start,end = 0,max(tree)

while start <= end :
    mid = (start + end) // 2
    result = 0
    for i in range(N) :
        if tree[i] > mid :
            result += tree[i] - mid
    if result >= M :
        start = mid + 1
        h = mid
    else :
        end = mid - 1
print(h)