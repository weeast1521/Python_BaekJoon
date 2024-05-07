import heapq
import sys
input = sys.stdin.readline

N = int(input())

min_heap = []
max_heap = []
result = []
if N == 1:
    print(int(input()))

else:
    tmp1 = int(input())
    tmp2 = int(input())
    if tmp1 >= tmp2:
        heapq.heappush(max_heap,-tmp2)
        heapq.heappush(min_heap,tmp1)
        result.append(tmp1)
        result.append(tmp2)
        for i in range(N-2):
            heapq.heappush(min_heap, int(input()))

            if len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -(heapq.heappop(min_heap)))
            if (-max_heap[0]) > min_heap[0]:
                tmp_min = heapq.heappop(min_heap)
                tmp_max = heapq.heappop(max_heap)
                heapq.heappush(max_heap,-tmp_min)
                heapq.heappush(min_heap,-tmp_max)
            result.append(-max_heap[0])
    else:
        heapq.heappush(max_heap,-tmp1)
        heapq.heappush(min_heap,tmp2)
        result.append(tmp1)
        result.append(tmp1)
        for i in range(N-2):
            heapq.heappush(min_heap, int(input()))

            if len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -(heapq.heappop(min_heap)))
            if (-max_heap[0]) > min_heap[0]:
                tmp_min = heapq.heappop(min_heap)
                tmp_max = heapq.heappop(max_heap)
                heapq.heappush(max_heap,-tmp_min)
                heapq.heappush(min_heap,-tmp_max)
            result.append(-max_heap[0])
print(*result, sep="\n")