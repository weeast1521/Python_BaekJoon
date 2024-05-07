N = int(input())

pipe = [list(map(int, input().split())) for _ in range(N)]

result = 0

def my_pipe(col, low, ex_pipe): # ex_pipe = 0(가로) , 1(세로), 2(대각선)
    if col == N-1 and low == N-1:
        result = result + 1
        return 0
    if ex_pipe == 0:
        

print(result)
