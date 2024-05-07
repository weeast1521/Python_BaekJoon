N, B = map(int,input().split())

l = []

while(True):
    if N == B:
        l.append(0)
        l.append(1)
        break
    elif N < B:
        l.append(N)
        break
    l.append(N % B)
    N // B == N
        
for i in range(len(l)):
    if l[i] > 9:
        l[i] = chr(l[i] + 55)

print(l[::-1])
