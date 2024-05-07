import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())

listen = []
not_listen = []

for i in range(N):
    tmp = input()
    listen.append(tmp)

for j in range(M):
    tmp = input()
    not_listen.append(tmp)

listen = set(listen)
not_listen = set(not_listen)

listen_not_listen = listen & not_listen
listen_not_listen = list(listen_not_listen)
listen_not_listen.sort()

print(len(listen_not_listen))
for i in listen_not_listen:
    print(i)
