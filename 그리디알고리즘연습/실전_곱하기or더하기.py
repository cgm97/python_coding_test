# 곱하기 혹은 더하기
# 507 page

arr = list(map(int,input().split()))

result = 0

for i in arr:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i
print(result)
    