S = input() # len(S) < 1000
S_list = []

for i in range(len(S)): # O(N)
    S_list.append(S[i:len(S)])

S_list.sort() # O(NlogN)

for i in S_list: # O(N)
    print(i)