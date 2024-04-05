import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    tmp = int(input())
    
    if tmp == 0:
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print(0)
            # pass
    else:
        heapq.heappush(heap, tmp)

# heappop을 할 때 빈 list이면 index out of range 오류가 나옴
# try except문을 이용해서 예외처리
# heapq는 최소힙(루트 노드가 가장 작은 수)를 기준으로 만들어짐