N = int(input())

stack = []
tmp = []

def check(index): # O(1)
    if tmp[index][0] == "push":
        stack.append(tmp[index][1])
    elif tmp[index][0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif tmp[index][0] == "size":
        print(len(stack))
    elif tmp[index][0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

for _ in range(N): # O(N)
    tmp.append(list(map(str,input().split())))

for i in range(N): # O(N)
    check(i)