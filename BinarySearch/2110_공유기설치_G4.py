# 단순한 좌표 index를 통한 이분탐색이 아닌 거리 자체에 대한 이분 탐색으로 최소 거리, 최대 거리에서 특정 만족 값을 좁혀나가는 이분 탐색 문제
import sys
input = sys.stdin.readline

N, C = map(int,input().split())
# N < 200,000 , home 좌표값 < 1,000,000,000
home = []

for i in range(N): # O(N)
    home.append(int(input()))

home.sort() # O(NlogN)

start = 1
end = home[-1] - home[0]
result = 0

if C == 2:
    print(home[-1] - home[0])
else:
    while(start < end): # O(N * log10^9) => 이분탐색 범위가 최대 거리에서 1까지 이므로 NlogN이 아닌 log10^9
        mid = (start + end) // 2
        count = 1
        temp = home[0]

        for i in range(N): # O(N)
            if home[i] - temp >= mid:
                count += 1
                temp = home[i]
            
        if count >= C:
            result = mid
            start = mid + 1
        else:
            end = mid

    print(result)