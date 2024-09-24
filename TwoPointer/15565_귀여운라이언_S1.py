N, K = map(int,input().split())
# N < 1,000,000
dolls = list(map(int,input().split()))

lion = []

if dolls.count(1) < K: # O(N)
    print(-1)

else:
    for index in range(N): # O(N)
        if dolls[index] == 1:
            lion.append(index)

    start = 0
    MIN = 10000000

    while(start + K <= len(lion)): # O(N)
        if lion[start + K - 1] - lion[start] + 1 < MIN:
            MIN = lion[start + K - 1] - lion[start] + 1
        start += 1
    print(MIN)

# 0 4 6 9 --> 4개