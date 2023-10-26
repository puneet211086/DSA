def numberInAnArray(a,x):
    if a[0]==x:
        return True
    if numberInAnArray(a[1:],x) == False:
        return False
    return True
        


a = [1,3,4,6,11,2]
x = 8

print(numberInAnArray(a,x))