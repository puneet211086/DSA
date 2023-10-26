def nthFibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    
    return nthFibonacci(n-1) + nthFibonacci(n-2)

    


print(nthFibonacci(0))