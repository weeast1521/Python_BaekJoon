import sys
input = sys.stdin.readline

N = int(input())
# N < 1,000,000

l = []

for i in range(N): # O(N)
    l.append(int(input()))

l.sort() # O(NlogN)

for i in l[::-1]: # O(N)
    print(i)


# 단순히 big-O 표기법으로는 시간초과가 뜰 일이 없지만 시간초과가 뜨는 문제