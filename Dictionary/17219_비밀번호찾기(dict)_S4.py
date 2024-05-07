import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())

password = {}

for _ in range(N):
    site, pw = input().split() #split을 해도 여기서는 str로 반환을 해주는구나 2개만 받으면 list가 아니라
    # site, pw = list 원소들이 unpack된다.

    password[site] = pw

for _ in range(M):
    site = input()
    print(password[site])