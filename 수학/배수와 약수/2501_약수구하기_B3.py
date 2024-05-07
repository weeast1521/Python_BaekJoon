N, M = map(int, input().split())

count = 0

for i in range(1,N+1):
    if N % i == 0:
        count = count + 1
    
    if count == M:
        print(i)
        break

if count < M:
    print(0)