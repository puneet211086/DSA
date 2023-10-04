class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def inputLL():
    inputData = [int(ele) for ele in input().split()]
    head = None 
    for data in inputData:
        if data == -1:
            break
        newNode = Node(data)
        if head == None:
            head = newNode
        else:
            curr = head 
            while curr.next is not None:
                curr = curr.next 
            curr.next = newNode
    return head


def printLL(head):
    curr = head 
    while curr is not None:
        print(curr.data,end="->")
        curr = curr.next 
    print("None")


head = inputLL()
printLL(head)


