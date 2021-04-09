def solution(array, commands):
    answer = []
    for command in commands :
        i,j,k = command
        new = array[i-1:j]
        new.sort()
        answer.append(new[k-1])
    return answer
