class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def __percolateUp(self):
        childIndex = len(self.pq)- 1
        
        while childIndex > 0:
            parentIndex = (childIndex - 1) //2
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break    


    def insertNode(self,value,priority):
        newNode = PriorityQueueNode(value,priority)
        self.pq.append(newNode)
        self.__percolateUp()

    
    def __percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2*parentIndex + 1
        rightChildIndex = 2*parentIndex + 2

        while leftChildIndex < len(self.pq):
            minIndex = parentIndex
            if self.pq[minIndex].priority > self.pq[leftChildIndex].priority:
                minIndex = leftChildIndex
            if rightChildIndex < len(self.pq) and self.pq[rightChildIndex].priority < self.pq[minIndex].priority:
                minIndex = rightChildIndex
            if minIndex == parentIndex:
                break

            self.pq[minIndex],self.pq[parentIndex] = self.pq[parentIndex],self.pq[minIndex]    
            parentIndex = minIndex
            leftChildIndex = 2*parentIndex +   1
            rightChildIndex = 2*parentIndex + 2

    
    def removeNode(self):
        e = self.pq[0]
        self.pq[0] = self.pq[len(self.pq)-1]
        self.pq.pop()
        self.__percolateDown()    



testpq = PriorityQueue()
testpq.insertNode("a",1)
testpq.insertNode("v",4)
testpq.insertNode("f",5)
testpq.insertNode("h",3)
testpq.insertNode("n",0)


for i in range(5):
    print(testpq.pq[i].priority)

print("------")

testpq.removeNode()
for i in range(4):
    print(testpq.pq[i].priority)

print("------")

    

testpq.removeNode()
for i in range(3):
    print(testpq.pq[i].priority)    


print("------")

    

testpq.removeNode()
for i in range(2):
    print(testpq.pq[i].priority)  


print("------")

    

testpq.removeNode()
for i in range(1):
    print(testpq.pq[i].priority)  

