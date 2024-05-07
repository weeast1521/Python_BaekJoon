N = input()
index = 0
count = 0

while(index < len(N)):
    if index == (len(N) - 1):
        count = count + 1
        break

    tmp = N[index]

    if tmp == 'd':
        if N[index + 1] == 'z':
            if (index + 1) == len(N)-1:
                count = count + 1
                index = index + 1
            elif N[index + 2] == '=':
                count = count + 1
                index = index + 3
            else:
                count = count + 1
                index = index + 1
        elif N[index + 1] == '-': 
            count = count + 1
            index = index + 2
        else:
            count = count + 1
            index = index + 1
    elif tmp == 'c':
        if N[index + 1] == '=' or N[index + 1] == '-':
            count = count + 1
            index = index + 2
        else:
            count = count + 1
            index = index + 1
    elif tmp == 'l' or tmp == 'n':
        if N[index + 1] == 'j':
            count = count + 1
            index = index + 2
        else:
            count = count + 1
            index = index + 1
    elif tmp == 's' or tmp == 'z':
        if N[index + 1] == '=':
            count = count + 1
            index = index + 2
        else:
            count = count + 1
            index = index + 1
    else:
        count = count + 1
        index = index + 1                      
print(count)