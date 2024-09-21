n = int(input()) # n < 100,000
l = list(map(int,input().split()))
l.sort() # O(NlogN)
x = int(input())

count = 0
s = 0
e = n - 1

while(s < e): # O(N)
    temp_sum = l[s] + l[e]

    if temp_sum > x:
        e -= 1
    elif temp_sum == x:
        s += 1
        e -= 1
        count += 1
    else:
        s += 1

print(count)