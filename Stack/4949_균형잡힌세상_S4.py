import sys
input = sys.stdin.readline

stack = ["0"]

while(True):
    string = input()

    if string[0] == ".":
        break

    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[":
            stack.append(string[i])
        elif string[i] == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif string[i] == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break

if len(stack) == 1:
    print("yes")
else:
    print("no")
        