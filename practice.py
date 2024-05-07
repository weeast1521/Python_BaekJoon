import sys
input = sys.stdin.readline

M = int(input()) #  M ≤ 3,000,000 300만

A = 'add'
R = 'remove'
C = 'check'
T = 'toggle'
ALL = 'all'
E = 'empty'

my_set = set({})
set_20 = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
set_0 = set({})

for i in range(M):
    my_list = input().split()
    tmp = my_list[0]
    if tmp == A:
        my_set.add(my_list[1])
    elif tmp == R:
        my_set = my_set - set(my_list[1])
    elif tmp == C:
        if len(my_set - set(my_list[1])) == len(my_set):
            print(0)
        else:
            print(1)
    elif tmp == T:
        if my_list[1] in my_set:
            my_set = my_set - set(my_list[1])
        else:
            my_set = my_set | set(my_list[1])
    elif tmp == ALL:
        my_set = set_20
    elif tmp == E:
        my_set = set_0
