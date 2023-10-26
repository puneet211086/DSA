def firstIndex(a,x):
    l = len(a)
    if l <= 0:
        return -1
    if a[0]==x:
        return 0

    smallList = a[1:]
    if firstIndex(smallList,x) ==-1:
        return -1
    else:
        return firstIndex(smallList,x) +1
    

a = [1,2,3,4,6]
x = 3
print(firstIndex(a,x))
