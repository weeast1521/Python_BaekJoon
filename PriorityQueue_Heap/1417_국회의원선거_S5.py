import heapq
import sys
input = sys.stdin.readline

N = int(input())
# N < 50

score = []
result = 0
num1 = int(input())

if N == 1:
	print(0)
else:
	for i in range(N-1): # O(N * logN)
		heapq.heappush(score, -int(input()))

	while(True):
		temp = -heapq.heappop(score)
		if temp >= num1:
			result += 1
			num1 += 1
			heapq.heappush(score, -(temp-1))
		else:
			break

	print(result)
	
# heappush() -> logN
# heappop() -> logN
# heapify() -> NlogN