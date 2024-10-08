from collections import defaultdict

N = int(input()) # N < 1,000,000
l = list(map(int, input().split()))

temp_l = l.copy() # O(N)
temp_l.sort() #O(NlogN)

dic = defaultdict(int)

count = 1
dic[temp_l[0]] = 0
temp = temp_l[0]

for i in range(1,N): #O(N)
    if(temp_l[i] != temp):
        dic[temp_l[i]] = count
        temp = temp_l[i]
        count += 1

for i in l:
    print(dic[i], end = " ")

# -10 -9 2 4 4 5
# 0   1  2 3 3 