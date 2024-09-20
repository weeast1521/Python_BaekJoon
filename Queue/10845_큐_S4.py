import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()
tmp = []

def check(index):
    if tmp[index][0] == "push":
        queue.append(tmp[index][1])

    elif tmp[index][0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif tmp[index][0] == "size":
        print(len(queue))

    elif tmp[index][0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif tmp[index][0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])        

for _ in range(N): # O(N)
    tmp.append(list(map(str,input().split())))

for i in range(N): # O(N)
    check(i)