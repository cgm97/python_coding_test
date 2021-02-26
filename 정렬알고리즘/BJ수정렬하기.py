# N개의 수가 주어 졌을 경우 이를 오름차순으로 정렬 하는
# 프로그램 작성

import sys

case = int(input())
result = [0 for i in range(10001)]
for num in sys.stdin:
    result[int(num)] += 1

for i in range(10001):
    if result[i] > 0:
        for j in range(result[i]):
            print(i)
    