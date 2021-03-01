# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

arr_num = (int(input()))

word_arr = []
for _ in range(arr_num) :
    word_arr.append(input())
word_arr_set = list(set(word_arr)) # 중복 제거

word_arr_set_list = []

for i in word_arr_set :
    word_arr_set_list.append((len(i),i))
word_arr_set_list.sort()

for lengh, i in word_arr_set_list :
    print(i)