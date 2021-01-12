# 숫자 카드 게임
# 96 page

# 입력
n,m = map(int,input().split())
result = 0
# n*m 배열 생성
for n in range(n) :
    data = list(map(int,input().split()))
    min_value = 10001
    # n행의 가장 작은 수
    min_value = min(data)
    # n행들의 가장 작은 수 중의 제일 큰값
    result = max(result,min_value)
print(result)

# 2중 반복문 사용
for n in range(n) :
    data = list(map(int,input().split()))
    min_value = 10001
    for m in data :
        # n행의 가장 작은 수
        min_value = min(min_value,m)
    # n행들의 가장 작은 수 중의 제일 큰값
    result = max(result,min_value)
print(result)