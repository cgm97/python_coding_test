def check(num): # 소수 판별 함수
    for i in range(2,num) :
        if num % i == 0 : # 자기자신으로만 나누어떨어져야한다
            return False
    return True

def solution(nums):
    answer = 0
    for i in range(len(nums)) :
        for j in range(i+1,len(nums)) :
            for k in range(j+1,len(nums)) :
                if check(nums[i] + nums[j] + nums[k]) :
                    answer+=1
    return answer
