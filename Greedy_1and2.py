
#######  1. 거스름돈 - 그리디 알고리즘 86 page
n = 1260
type = [500,100,50,10]
count = 0

for coin in type :
    count = count + (n // coin)
    n = n % coin
print(count)

#######  2. 큰수의 법칙 - 그리디 알고리즘 92 page
n,m,k = map(int,input().split())
data = list(map(int,input().split()))
# print(data) # ['1', '2', '3', '4', '5'] - 리스트 배열 생성
data.sort()  # 작은수 정렬
first = data[n-1] # 가장 큰수
second = data[n-2] # 두번째 큰수
result = 0

# 반복문으로 풀이
while True:
    for i in range(0,k):
        if m == 0 :
            break
        else :
            result += first
            m -= 1
            print("up")
            print(result)
    if m == 0 :
        break
    else : 
        result += second
        m -= 1
        print("down")
        print(result)
print(result)

# 수학적으로 풀이
count = int(m/(k+1)*k) # 큰 수의 반복 횟수
count += m%(k+1) # 나누어 떨어지지않으면 +n번 반복 추가

result += count * first
result += (m-count)*second # (총 횟수 - 큰 수 반복 횟수) = 작은수의 더하는 횟수

print(result)

# for i in range(0,k+1):
#     for i in range(0,k):
#         if m == 0 :
#             break
#         else :
#             result += first
#             m -= 1
#             print("up")
#             print(result)
#     if m == 0 :
#         break
#     else : 
#         result += second  
#         m -= 1
#         print("down")
#         print(result)