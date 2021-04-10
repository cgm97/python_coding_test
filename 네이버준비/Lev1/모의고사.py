def solution(answers):
    result = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    p1c = 0
    p2c = 0
    p3c = 0
    
    for i in range(len(answers)) :
        if answers[i] == p1[i%5] : #i%문제수 를 해야 런타임 오류가 안뜸
            p1c += 1               #처음엔 i 로 했으나 런타임 오류 발생
        if answers[i] == p2[i%8] :
            p2c += 1
        if answers[i] == p3[i%10] :
            p3c += 1
    answer_ary = [p1c,p2c,p3c]
    
    for i , j in enumerate(answer_ary) : # enumerate -> (인덱스,값) 이렇게 출력 해줌
        if j == max(answer_ary) :
            result.append(i+1) # 가장 큰 값인 인덱스를 result에 추가
    return result
