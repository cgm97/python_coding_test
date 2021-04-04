def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    
    while progresses :
        if progresses[0] + day * speeds[0] >= 100 :
            progresses.pop(0) # 작업완료 했으니 삭제
            speeds.pop(0) 
            count += 1 #완료된 현재 개수
        else :
            if count > 0 : #현재 day 일 만큼 완료된 작업의 개수 추가
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)        
    return answer
