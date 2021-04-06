# 1안) - 95.8점 실패
def solution(phone_book):
    sort = sorted(phone_book)
    result = True
    for i in range(len(phone_book)-1) :
        if sort[i] in sort[i+1] :
            result = False
            break
    return result

# 2안) - 100점 성공
def solution(phone_book):
    phone_book.sort()
    result = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            result = False
            break
    return  result
# 찾을대상.startwith(찾고자하는문자) => 있으면 True 없으면 False 반환
