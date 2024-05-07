import sys
input = sys.stdin.readline

N, Q = map(int,input().split())
# N < 200,000 , Q < 200,000

N_sequence = [0] + list(map(int,input().split()))

N_sequence2 = []
for i in range(Q): #O(N)
    tmp = list(map(int,input().split()))

    if tmp[0] == 3:
        print(sum(N_sequence[tmp[1]:tmp[2]+1]))
    elif tmp[0] == 1:
        if tmp[1] != N:
            N_sequence2 = [0]+ N_sequence[N-tmp[1]+1: N+1] + N_sequence[1:N-tmp[1]]
            N_sequence = N_sequence2
    else:
        if tmp[1] != N:
            N_sequence2 = [0]+ N_sequence[tmp[1]+1: N+1] + N_sequence[1:tmp[1]+1]
            N_sequence = N_sequence2
        
