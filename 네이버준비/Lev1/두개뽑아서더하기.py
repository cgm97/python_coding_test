#1) 내가 했던 방법 -> 복잡도 문제 발생
def solution(numbers)
    answer = []
    for i in range(len(numbers)-1) 
        for j in range(i+1,len(numbers)) 
            answer.append(numbers[i]+numbers[j])
    answer.sort()
    return list(set(answer))

#2) 다른 사람의 풀이
# 나와 비슷하게 풀었지만 복잡도 문제 해결 할 수 있었다.
def solution(numbers)
    answer = []
    for i in range(len(numbers)-1) 
        for j in range(i+1,len(numbers)) 
            if numbers[i]+numbers[j] not in answer
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer
