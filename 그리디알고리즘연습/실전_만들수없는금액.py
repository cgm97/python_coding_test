# 만들 수 없는 금액
# 509 page

num = list(map(int,input().split()))
sum=1
for i in num:
    if sum < i:
        break
    sum += i

print(sum)