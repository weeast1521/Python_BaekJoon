N = input().upper()

result = list(set(N))
result_num = [0] * len(result)
for i in range(len(N)):
    for j in range(len(result)):
        if N[i] == result[j]:
            result_num[j] = result_num[j] + 1
            break

big = max(result_num)

tmp = result_num.count(big)

if tmp == 1:
    index = result_num.index(big)
    print(result[index])
else:
    print("?")

'''
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])
'''
#find 함수는 string 문자열에서만 가능하고 index 함수는 리스트에서도 가능하다.
#count 함수는 문자열에서 그 문자가 몇개인지 알려준다.
#join() 메서드는 파이썬에서 문자열을 결합하고 합친 문자열을 반환
#f-string은 문자열의 앞에 f 글자를 붙인 문자열을 의미하며 {} 안에서
# 변수의 이름을 바로 사용할 수 있기 때문에 가독성도 높고 편리하여 가장 진보된 방식으로 평가됩니다.
# https://velog.io/@goplanit/Algorithm-%EB%B0%B1%EC%A4%80-1157%EB%B2%88-%EB%8B%A8%EC%96%B4-%EA%B3%B5%EB%B6%80%ED%8C%8C%EC%9D%B4%EC%8D%AC