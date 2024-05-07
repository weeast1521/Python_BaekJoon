index = 0

while True:
    pizza = list(map(int,input().split()))
    index = index + 1
    if pizza[0] == 0:
        break

    if pizza[0] * pizza[0] >= ((pizza[1] * pizza[1]) / 4) + ((pizza[2] * pizza[2]) /4):
        print("Pizza {} fits on the table." .format(index))
    else:
        print("Pizza {} does not fit on the table." .format(index))
