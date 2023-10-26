def oneToN(n):
    if n ==0:
        return
    oneToN(n-1)
    print(n)

oneToN(5)

