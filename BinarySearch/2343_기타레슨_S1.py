import sys
input = sys.stdin.readline

N, M = map(int,input().split())
# N < 100,000
blue = list(map(int,input().split()))

start = max(blue)
end = sum(blue)
result = 0 # blueray의 크기
# 강의의 최대 길이 10,000

while(start <= end): # O(N * log(10,000N))
    mid = (start + end) // 2

    count = 1
    temp_sum = 0

    for i in range(N): # O(N)
        if temp_sum + blue[i] <= mid:
            temp_sum += blue[i]
        else:
            count += 1
            temp_sum = blue[i]
    
    if count <= M:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)