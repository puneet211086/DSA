def sumOfAnArray(a):
    if len(a)==1:
        return a[0]
    
    return a[0] + sumOfAnArray(a[1:])


a = [1,2,5,6]
print(sumOfAnArray(a))


