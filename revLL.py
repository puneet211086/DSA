class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def inputLL():
    getData = [int(ele) for ele in input().split()]
    head=None
    for data in getData:
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

def printData(head):
    curr = head
    while curr is not None:
        print(curr.data,end="->")
        curr = curr.next
    print("None")



def revLL(head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev    


head1 = inputLL()
printData(head1)
head2 = revLL(head1)
printData(head2)
