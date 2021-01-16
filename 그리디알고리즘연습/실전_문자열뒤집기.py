# 문자열 뒤집기
# 508 page

arr = input()

count0=0
count1=0

if arr[0] == '0' :
    count1+=1
else :
    count0+=1

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == '1':
            count0+=1
        else:
            count1+=1
    
print("0 -> 1 ",count1,"번")
print("1 -> 0 ",count0,"번")