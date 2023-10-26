class PrioirityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def __percolateUp(self):
        childIndex = len(self.pq)- 1
        while childIndex > 0:
            parentIndex = (childIndex -1)//2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break    




    def insert(self,value,priority):
        newNode = PrioirityQueueNode(value,priority)
        self.pq.append(newNode)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2*parentIndex + 1
        rightChildIndex = 2*parentIndex + 2
        minIndex =0

        while leftChildIndex < len(self.pq)-1:
            if self.pq[minIndex].priority > self.pq[leftChildIndex].priority:
                minIndex = leftChildIndex
            if rightChildIndex < len(self.pq)-1 and self.pq[rightChildIndex].priority < self.pq[minIndex]:
                minIndex = rightChildIndex
            if minIndex == parentIndex:
                break
            self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
            parentIndex = minIndex
            leftChildIndex = 2*parentIndex + 1 
            rightChildIndex = 2*parentIndex + 2





    def removeMin(self):
        e = self.pq[0]
        self.pq[0]=self.pq[len(self.pq)]
        self.pq.pop()
        self.percolateDown()

            
