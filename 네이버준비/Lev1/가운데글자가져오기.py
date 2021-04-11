def solution(s):
    answer = len(s) // 2
    if len(s) % 2 == 1:      
        return s[answer]
    else :
        return s[answer-1:answer+1]
