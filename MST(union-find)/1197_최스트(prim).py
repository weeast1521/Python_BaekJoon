import heapq
import sys
input = sys.stdin.readline


V, E = map(int, input().split())
# 1 <= V <= 10,000 , 1 <= E <= 100,000
mst = []
sum_w = 0
connect = [False] * (V+1)

for _ in range(E): # O(N)
    edge = list(map(int, input().split()))
    mst.append(edge)