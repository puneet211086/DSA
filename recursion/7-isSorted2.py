def isSorted2(a,si):
    if si == len(a)-1 or si ==0:
        return True

    if a[si] > a[si+1]:
        return False
    return isSorted2(a,si+1)


a = [1,2,3,4,5,7]

print(isSorted2(a,0))
        