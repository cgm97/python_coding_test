# 1) 가독성이 좋지 않은 방법
def solution(clothes):
    result = 1
    spy = {}
    
    for i in range(len(clothes)) :
        # 오늘입은 복장의 종류 spy 딕셔너리에 추가 => 개수는 1개
        if clothes[i][1] not in spy :
            spy[clothes[i][1]] = 1
        # 오늘입은 복장의 종류가spy에 존재한다면 => 1씩 추가
        else :
            spy[clothes[i][1]] += 1
            
    
    for key in spy:
        result *= (spy[key]+1)
    return result - 1

    # 조합 개수 계산법
    # 모든 옷 조합수 = (종류+1) * (종류+1) - 1 이다.


# 2) 가독성이 더 좋은 방법
def solution(clothes):
    result = 1
    spy = {}
    
    for cloth,c_type in clothes :
        # 오늘입은 복장의 종류 spy 딕셔너리에 추가 => 개수는 1개
        if c_type not in spy :
            spy[c_type] = 1 # "종류",1 로 저장됨
        # 오늘입은 복장의 종류가spy에 존재한다면 => 1씩 추가
        else :
            spy[c_type] += 1
            
    
    for key in spy.values():
        result *= (key+1)
    return result - 1

    # 조합 개수 계산법
    # 모든 옷 조합수 = (종류+1) * (종류+1) - 1 이다.

