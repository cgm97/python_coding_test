def solution(participant, completion):
    participant.sort() # 문자 정렬
    completion.sort()  # 문자 정렬
    # 각 배열을 문자순으로 정렬 한 뒤
    # 두개의 배열을 0번지 부터 비교하여 일치 하지않으면 해당 번지의 선수는 
    # 완주 하지 못함 -> 출력
    # 만약 전부 다 일치하여 없을시 마지막 문자의 선수는 미완주
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]
    return participant[i+1]
