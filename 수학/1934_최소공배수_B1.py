T = int(input())

for i in range(T):
    a, b = map(int,input().split())
    if a > b:
        a, b = b, a
    count = a
    while(a>0):
        if a % count == 0 and b % count == 0:
            break
        count = count - 1
    print(a*int(b/count))
