import heapq
import sys
input = lambda : sys.stdin.readline().strip()

N = int(input()) # N < 100,000

plus = []
minus = []

plus_count = 0
minus_count = 0

for _ in range(N):
    temp = int(input())
    if temp == 0:
        if plus_count == 0 and minus_count == 0:
            print(0)
        elif plus_count == 0 and minus_count != 0:
            print(-heapq.heappop(minus))
            minus_count -= 1
        elif plus_count != 0 and minus_count == 0:
            print(heapq.heappop(plus))
            plus_count -= 1
        else:
            if plus[0] >= minus[0]:
                print(-heapq.heappop(minus))
                minus_count -= 1
            else:
                print(heapq.heappop(plus))
                plus_count -= 1
    elif temp > 0:
        heapq.heappush(plus, temp)
        plus_count += 1
    else:
        heapq.heappush(minus, -temp)
        minus_count += 1

 