class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inputBinaryTree():
    rootData=int(input())
    if rootData == -1:
        return
    root = BinaryTreeNode(rootData)
    root.left = inputBinaryTree()
    root.right=inputBinaryTree()

    return root


def printBinaryTree(root):
    if root == None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print("L",root.left.data,end=",")
    if root.right is not None:
        print("R",root.right.data,end="")
    print()
    printBinaryTree(root.left)
    printBinaryTree(root.right)


def numberNodes(root):
    if root == None:
        return 0
    sum = 1
    numLeft = numberNodes(root.left)
    numRight = numberNodes(root.right)
    return sum + numLeft+numRight

def sumNodes(root):
    if root == None:
        return 0
    leftSum = sumNodes(root.left)
    rightSum= sumNodes(root.right)

    return root.data+ leftSum +rightSum 


def preOrder(root):
    if root==None:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def inOrder(root):
    if root ==None:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def nodeWithLargestData(root):
    if root == None:
        return -1
    leftLargest = nodeWithLargestData(root.left)
    rightLargest = nodeWithLargestData(root.right)
    return max(root.data,leftLargest,rightLargest)


def nodesGreaterX(root,x):
    if root == None:
        return 0
    
    leftGtx = nodesGreaterX(root.left,x)
    rightGtx = nodesGreaterX(root.right,x)
    if root.data > x:
        return 1 + leftGtx + rightGtx
    return leftGtx + rightGtx

def heightOfTree(root):
    if root == None:
        return 0
    leftHeight = heightOfTree(root.left)
    rightHeight = heightOfTree(root.right)
    return 1 + max(leftHeight,rightHeight)

def numberOfLeaf(root):
    if root == None:
        return 0
    
    if not root.left and not root.right:
        return 1
    leftleaf = numberOfLeaf(root.left)
    rightLeaf = numberOfLeaf(root.right)
    return leftleaf + rightLeaf 

def printAllNodesDepthK(root,k):
    if root == None:
        return
    if k == 0:
        print(root.data)  
        return  
    printAllNodesDepthK(root.left,k-1)
    printAllNodesDepthK(root.right,k-1)

def printAllNodesDepthK2(root,k,d=0):
    if root == None:
        return
    if k==d:
        print(root.data)
        return

    printAllNodesDepthK2(root.left,k,d+1)
    printAllNodesDepthK2(root.right,k,d+1)




    

root1 = inputBinaryTree()
# printBinaryTree(root1)
# print(numberNodes(root1))
# print(sumNodes(root1))

# print("Pre_____________")
# preOrder(root1)
# print("Post____________")
# postOrder(root1)
# print("In______________")
# inOrder(root1)

# print(nodeWithLargestData(root1))

# print(nodesGreaterX(root1,3))

# print(heightOfTree(root1))

# print(numberOfLeaf(root1))

#printAllNodesDepthK(root1,2)

printAllNodesDepthK2(root1,2)