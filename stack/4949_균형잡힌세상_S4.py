while(True):
    string = input()

    if string == ".":
        break

    stack = [-1]
    check = True

    for i in string:
        if i == "(":
            stack.append(0)
        elif i == ")":
            if stack.pop() != 0:
                check = False
                break
        elif i == "[":
            stack.append(1)
        elif i == "]":
            if stack.pop() != 1:
                check = False
                break
            
    if len(stack) != 1:
        check = False

    if check:
        print("yes")
    else:
        print("no")