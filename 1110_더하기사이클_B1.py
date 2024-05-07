N = input()
origin_N = N
count = 0

while(True):
    count = count + 1
    if len(N) == 1:
        N + '0'
    elif N[0] == '0':
        N = N[1] + '0'
    
    tmp = N[-1]

    N = int(N[0]) + int(N[-1])
    N = str(N)

    N = tmp + N[-1]
    
    if origin_N == N:
        print(count)
        break

# 55 == 10 -> 50 == 5 -> 05 == 5 -> 55