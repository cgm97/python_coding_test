# 숫자 카드 게임

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