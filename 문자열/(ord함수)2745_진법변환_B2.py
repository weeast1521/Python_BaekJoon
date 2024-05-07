N, B = input().split()
N_list = list(N)
N_list.reverse()
B = int(B)
index = 0
result = 0


for value in N_list:
    if ord(value) < 60:
        tmp = int(value) * (B ** index)
    else:
        tmp = (ord(value) - 55) * (B ** index)
    result = result + tmp
    index = index + 1

print(result)
