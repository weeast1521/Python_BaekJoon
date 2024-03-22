N = int(input())

DP = [0] * (N + 1)

for i in range(2, N+1): # 1로 뺐을때, 2로 나누었을때, 3으로 나누었을때 최소값을 찾아야하기에 이렇게 함
    DP[i] = DP[i-1] + 1
    
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)
    
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)

print(DP[N])