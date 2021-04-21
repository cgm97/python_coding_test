N = int(input())
M = int(input())
recommand = list(map(int,input().split()))
photo = [] # 사진틀
score = [] # 추천수

for i in range(M) :
    if recommand[i] in photo : # 추천 한 사람이 액자에 있을 경우
        for j in range(len(photo)) : # 액자에서 해당된 사람 위치를 찾고
            if recommand[i] == photo[j] : # 해당 액자 위치에 추천수 증가
                score[j] += 1
    else :
        if len(photo) >= N : # 액자의 크기가 3 이상이면 삭제 해야한다
            for k in range(len(photo)) : # 액자틀안의 추천수 조회
                if score[k] == min(score) : # 추천수가 가장 작고 오래된 사진틀 삭제
                    del photo[k]
                    del score[k]
                    break # 처음부터 조사 하는것이 오래된 사진틀이라 찾으면 종료
        photo.append(recommand[i]) # 추천인 없으면 추가
        score.append(1)            # 추가된 추천인 추천수 1로 초기 선언
photo.sort()

for result in photo :
    print(result,end=" ")