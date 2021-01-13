# 시각 - 구현
# 113 page
cnt = 0
for h in range(24):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                cnt+=1
                print(str(h)+str('시')+str(m)+str('분')+str(s)+str('초'))
print(cnt)