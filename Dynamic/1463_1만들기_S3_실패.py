N = int(input())

dp = [0] * 1000001

for i in range(3,N + 1): # 단순히 규칙을 찾았다고 생각함 예외가 매우 많음
    if i % 3 == 0:
        dp[i] = dp[i//3] + 1
    elif i % 2 == 0:
        dp[i] = dp[i//2] + 1 
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])