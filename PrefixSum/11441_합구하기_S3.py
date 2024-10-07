import sys
input = sys.stdin.readline

N = int(input()) # N < 100,000
l = list(map(int,input().split()))
M = int(input())

prefix_sum = [0]

for i in range(N): # O(N)
    prefix_sum.append(prefix_sum[i] + l[i])

for _ in range(M): # O(N)
    s, e = map(int,input().split())

    print(prefix_sum[e] - prefix_sum[s-1])