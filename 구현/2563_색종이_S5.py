import sys
input = sys.stdin.readline

N = int(input()) # N < 100

matrix = [[0]*100 for _ in range(100)]
result = 0

for i in range(N): # O(N)
    x, y = map(int,input().split())

    for i in range(x,x+10): # O(100)
        for j in range(y,y+10):
            matrix[i][j] = 1

for i in range(100): # O(10000)
    for j in range(100):
        if matrix[i][j] == 1:
            result += 1 

print(result)

# 전체를 좌표로 만들고 계산이 더 편함