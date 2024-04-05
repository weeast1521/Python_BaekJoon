import sys
input = sys.stdin.readline

T = int(input())

test_list = []

for i in range(T):
    test_list.append(int(input()))

DP = [0] * 5001
DP[0] = 1
DP[2] = 1

#(  )(),()(  ),(    ) => 큰 괄호들 모양에 따라 다르고 그 큰 괄호 두개 사이에 들어가는 갯수에 따라 DP값들이 들어가면 된다.

for i in range(4,5002,2):
    for j in range(0,i+1,2):
        DP[i] = DP[i] + DP[j]*DP[i-j-2]
    DP[i] = DP[i] % (int(1e9)+7)

for i in test_list:
    print(DP[i])
