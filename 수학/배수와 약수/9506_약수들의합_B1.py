while(True):
    n = int(input())

    if n == -1:
        break

    sum = 0
    factors = []

    for i in range(1,n):
        if n % i == 0:
            sum = sum + i
            factors.append(i)
    
    if sum == n:
        print(n, "=", end = " ")
        for i in range(len(factors)-1):
            print(factors[i], "+", end = " ")
        print(factors[-1])

    else:
        print(n, "is NOT perfect.")