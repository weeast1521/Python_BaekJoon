N, K = map(int, input().split())
l = list(map(int,input().split()))

l.sort() # O(NlogN)

print(l[K-1])