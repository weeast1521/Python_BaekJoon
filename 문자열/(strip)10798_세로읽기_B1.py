import sys
input = sys.stdin.readline

lines = []
for i in range(5):
    a = input().strip()
    lines.append(a)
    
for i in range(5):
    lines[i] = lines[i] + ("*" * (15 - len(lines[i])))
    
for i in range(15):
    for j in range(5):
        if lines[j][i] != "*":
    	    print(lines[j][i], end="")





#https://www.acmicpc.net/problem/10798 ??