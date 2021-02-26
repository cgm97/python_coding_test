# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

# 둘째 줄에는 중앙값을 출력한다.

# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

# 넷째 줄에는 범위를 출력한다.

import sys
from collections import Counter

N = int(input())
arr = []
for _ in range(N) : 
    arr.append(int(input()))
sortArr = sorted(arr)
mostbinarr = Counter(sortArr).most_common(2) # 최빈값 계산
if N > 1 : 
   if mostbinarr[0][1] == mostbinarr[1][1] :
        mostbin = mostbinarr[1][0]
   else :
        mostbin = mostbinarr[0][0]
else :
    mostbin = sortArr[0]
       
print(round(sum(sortArr)/N))
print(sortArr[N//2])
print(mostbin)
print(max(sortArr)-min(sortArr))
