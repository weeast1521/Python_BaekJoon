import sys
input = sys.stdin.readline

N, M = map(int,input().split())
# N, M < 300
matrix = []

for _ in range(N): # O(N)
    matrix.append([0]+list(map(int,input().split()))) # 0을 앞에 추가해 계산 편하게함

for floor in range(N): # 각 층마다 prefix sum 생성
    temp = 0
    for i in range(1,M+1):
        matrix[floor][i] += temp
        temp = matrix[floor][i]

K = int(input())
# K < 10,000

for _ in range(K): # O(K * N)
    i,j,x,y = map(int,input().split())

    result = 0

    for floor in range(i-1,x): # O(N)
        result = result + matrix[floor][y] - matrix[floor][j-1]
    
    print(result)