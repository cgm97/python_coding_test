# 모험가 길드
# 506 page

arr = list(map(int,input().split()))

arr.sort()

count=0 # 현재 그룹의 인원수
result=0 # 결성된 총 그룹의수

for i in arr:
    count+=1
    if i <= count:
        result += 1 # 그룹 결성
        count=0 # 다음 그룹 결성을 위해 초기화
print(result)
