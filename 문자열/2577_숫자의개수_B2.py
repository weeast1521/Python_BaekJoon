A = int(input())
B = int(input())
C = int(input())

temp = A*B*C

temp = str(temp)
num = [0] * 10
#count 함수를 써도 됨.
for i in temp: #문자열을 그냥 넣어도 되는구나
    if i == '0':
        num[0] = num[0] + 1
    elif i == '1':
        num[1] = num[1] + 1
    elif i == '2':
        num[2] = num[2] + 1
    elif i == '3':
        num[3] = num[3] + 1
    elif i == '4':
        num[4] = num[4] + 1
    elif i == '5':
        num[5] = num[5] + 1
    elif i == '6':
        num[6] = num[6] + 1
    elif i == '7':
        num[7] = num[7] + 1
    elif i == '8':
        num[8] = num[8] + 1
    elif i == '9':
        num[9] = num[9] + 1
for i in range(10):
    print(num[i])  