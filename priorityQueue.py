class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def __percolateUp(self):
        childIndex = len(self.pq)-1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex] = self.pq[parentIndex],self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,value,priority):
        newNode = PriorityQueueNode(value,priority)
        self.pq.append(newNode)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2*parentIndex+1
        rightChildIndex = 2*parentIndex+2

        while leftChildIndex < len(self.pq):
            minIndex = parentIndex
            if self.pq[minIndex].priority > self.pq[leftChildIndex].priority:
                minIndex = leftChildIndex
            if rightChildIndex < len(self.pq)  and self.pq[minIndex].priority > self.pq[rightChildIndex].priority:
                minIndex = rightChildIndex
            if parentIndex == minIndex:
                break

            self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
            parentIndex = minIndex
            leftChildIndex = 2*parentIndex+1
            rightChildIndex = 2*parentIndex+2



    
    def remove(self):
        ele = self.pq[0]
        self.pq[0] =self.pq[len(self.pq)-1]
        self.pq.pop()
        self.__percolateDown()
        return ele.value
    


def heapSort(a):
    heap = PriorityQueue()
    for i in range(len(a)):
        heap.insert(i,a[i])
    a = []    
    for i in range(heap.getSize()):
        a.append(heap.remove())
    print(a)   

        
heapSort([87,4,6,9,11,34,67])    







# a = PriorityQueue()
# a.insert("a",10)
# a.insert("g",4)
# a.insert("e",3)

# print(a.remove())
# print(a.remove())
# print(a.remove())