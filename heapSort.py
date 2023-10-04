class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)
    
    def insert(self,priority):
        newNode = PriorityQueueNode(priority)
        self.pq.append(newNode)
        childIndex = self.getSize() - 1
        while childIndex > 1:
            parentIndex = (childIndex -1)//2
            if self.pq[childIndex].priority > self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[childIndex]
                childIndex=parentIndex
            else:
                break
    
                   
