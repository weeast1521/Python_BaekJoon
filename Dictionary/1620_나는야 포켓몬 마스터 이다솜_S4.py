import sys
input = lambda : sys.stdin.readline().strip() # strip을 안붙이면 \n이 들어가서 오류 발생

N, M = map(int, input().split())

pocket_moster = {}
pocket_monster_num = {}

for i in range(1,N+1):
    name = input()

    pocket_moster[name] = i
    pocket_monster_num[i] = name

for _ in range(M):
    temp = input()
    if ord(temp[0]) < 65:
        print(pocket_monster_num[int(temp)])
    else:
        print(pocket_moster[temp])