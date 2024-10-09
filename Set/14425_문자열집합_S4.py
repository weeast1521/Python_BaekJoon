import sys
input = sys.stdin.readline

N, M = map(int,input().split())
# N < 10,000 , M < 10,000
s = set()
count = 0

for i in range(N): # O(N)
    s.add(input())

for i in range(M): #O(M)
    temp = input()

    if temp in s:
        count += 1

print(count)