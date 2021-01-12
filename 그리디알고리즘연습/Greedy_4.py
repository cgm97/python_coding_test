# 1이 될때 까지
# 99 page
# https://github.com/ndb796/python-for-coding-test/issues/37

# 입력
n,k = map(int,input().split())
result = 0
count = 0

# 나의 풀이과정_1
while n >= k:
    if n % k == 0 :
        n //= k
        count += 1
    if n == 1 :
        break
    n -= 1
    count += 1
print(count)

# 나의 풀이과정_2
while n !=1 :
    if n % k == 0 :
        n //= k
        count += 1
    else :
        n -= 1
        count += 1
print(count)

# 책 풀이과정
while True:
    #  n == k 로 나누어 떨어 질때까지 1씩 빼기
    target = (n // k) * k
    result += (n-target)
    n = target
    # n 이 k 보다 작을때(더이상 나눌수없음) 반복문 종료
    if n < k :
        break
    # k 로 나누기
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)