import sys
input= sys.stdin.readline #236 ms /// 없을때는 4256 ms 거의 20배 차이가

N = int(input()) # N < 100,000 # 제한시간 1초 # 회의실 2는 N이 25까지였음

Member_list = []

for i in range(N):
    Member_list.append(list(map(int, input().split())))

Member_list.sort()

DP = [0]*N
DP[0] = Member_list[0][2]

for i in range(1,N):
    DP[i] = max(DP[i-1],DP[i-2] + Member_list[i][2])

print(DP[N-1])