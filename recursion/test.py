def factorial(a):
    if a == 0:
        return 1
    return a*factorial(a-1)

# print(factorial(5))

def sumOfFirstN(a):
    if a == 0:
        return 0
    return a + sumOfFirstN(a-1)

# print(sumOfFirstN(5))

def powerOfANumber(a,x):
    if x==0:
        return 1
    return a*powerOfANumber(a,x-1)

# print(powerOfANumber(0,1))


def printOneToN(n):
    if n==0:
        return
    printOneToN(n-1)
    print(n)

# printOneToN(0)


def fibonacci(a):
    if a==1:
        return 1
    if a==2:
        return 1
    
    return fibonacci(a-1) + fibonacci(a-2)

# print(fibonacci(5))


def isSorted(a):
    l = len(a)
    if l == 0 or l==1:
        return True
    if a[0] > a[1]:
        return False
    return isSorted(a[1:])

print(isSorted([1]))




