N = list(map(int,input()))
N.sort() # O(NlogN)

SUM = sum(N) # O(N)

if N[0] != 0:
    print(-1)
elif SUM % 3 != 0:
    print(-1)
else:
    N = list(map(str, N)) #O(N)
    print("".join(N[::-1]))