from collections import defaultdict
S = input() # length <= 1000

# S_list = []
length = 1
count = 0
dic = defaultdict(int)

'''
while(length < len(S)+1): # O(N * N * N)
    for s in range(0,len(S)): # O(N)
        if S[s:s+length] not in S_list: # O(N)
            S_list.append(S[s:s+length])
    length += 1
    
    ==> 리스트를 이용해서 중복 제거 -> 시간초과 N^3
'''

'''
while(length < len(S)+1): # O(N * N * slicing)
    for s in range(0,len(S)): # O(N)
        if dic[S[s:s+length]] == 0: # O(slicing 시간복잡도)
            dic[S[s:s+length]] += 1
            count += 1
    
    length += 1    
print(count)
    ==> dictionary를 사용해서 중복 제거 시간초과는 안뜨지만 984ms
'''

s=input()
total=set()
for i in range(len(s)):
    for j in range(i,len(s)):
        total.add(s[i:j+1])#i번째 문자부터 부분문자열 구하기

print(len(total))

# set을 이용해서 중복제거 480ms로 가장 빠름