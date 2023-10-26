def isSorted(a):
    if len(a)==0 or len(a)==1:
        return True
    smallList = a[1:]

    if isSorted(smallList) and a[0] < smallList[0]:
        return True
    return False

a = [1,3,4,5]
print(isSorted(a))