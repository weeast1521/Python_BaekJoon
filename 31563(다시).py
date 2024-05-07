import sys
input = sys.stdin.readline

N, Q = map(int,input().split())
# N < 200,000 , Q < 200,000

N_sequence = list(map(int,input().split()))

prefix_sum = N_sequence[0]
prefix_sum_list = [N_sequence[0]]

for i in range(1,N):
    prefix_sum += N_sequence[i]
    prefix_sum_list.append(prefix_sum)

print(prefix_sum_list)