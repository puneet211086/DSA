def sumOfFirstN(n):
    if n ==0:
        return 0
    return n + sumOfFirstN(n-1)


print(sumOfFirstN(3))