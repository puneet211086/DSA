def lastIndex(a,x):
    l = len(a)
    if l <= 0:
        return -1
    
    smallList = a[1:]
    if lastIndex(smallList,x)==-1:
        if x==a[0]:
            return 0
        else:
            return -1
    else:
        return lastIndex(smallList,x)+1


a = [1,2,3,4]
x=3
print(lastIndex(a,x))
    