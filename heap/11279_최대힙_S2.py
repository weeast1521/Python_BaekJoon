import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    tmp = int(input())
    
    if tmp == 0:
        try:
            print(heapq.heappop(heap)[1])
        except IndexError:
            print(0)
            # pass 그냥 지나가고 싶으면 pass
    else:
        heapq.heappush(heap, (-tmp, tmp))

# heappop을 할 때 빈 list이면 index out of range 오류가 나옴
# try except문을 이용해서 예외처리
# heapq는 최소힙(루트 노드가 가장 작은 수)를 기준으로 만들어짐
# 따라서 최대힙(부모 노드가 자식 노드보다 큼)을 만들려면
# push(heap, (-tmp,tmp))로 하면 튜플의 첫번째 값을 기준으로 push
# 하기에 출력을 할 때 index [1]을 출력하면 최대 힙이 된다.