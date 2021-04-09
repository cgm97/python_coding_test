def solution(numbers):
    answer = ''
    result = list(map(str,numbers)) # 정수로 비교하면 원하는 방향으로 안되므로 문자열로 변환 하여 비교
    # 예를 들면 6 2 10 을 문자열 내림차순 정리 하기 위해
    # lambda x : x*3 사용 하여 666 222 101010 의 크기를 비교한다
    # 가장 큰 값은 666 그다음 222 그다음 101010 이다. 문자열 비교에서는
    result.sort(key=lambda x : x*3, reverse=True)
    if len(result) == result.count('0'):
        return '0'
    return answer.join(result)
