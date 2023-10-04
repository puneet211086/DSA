class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None


def inputBT():
    data = int(input())
    if data == -1:
        return None
    
    root = Node(data)
    root.left = inputBT()
    root.right = inputBT()
    return root

def printBT(root):
    if root == None:
        return None
    
    print(root.data,end=":")
    if root.left:
        print("L",root.left.data,end=",")
    if root.right:
        print("R",root.right.data,end="")
    print()

    printBT(root.left)
    printBT(root.right)

root1 = inputBT()
printBT(root1)            
