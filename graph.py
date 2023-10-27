class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]


    def insertNodes(self,x,y):
        self.adjMatrix[x][y]=1
        self.adjMatrix[y][x]=1

    def removeNodes(self,x,y):
        if self.adjMatrix[x][y]!=1 or self.adjMatrix[y][x]!=1:
            return
        self.adjMatrix[x][y] = 0
        self.adjMatrix[y][x] = 0

    def dfsHelper(self,sv,visited):
        print(sv)
        visited[sv] = True

        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]==1 and visited[i]==False:
                self.dfsHelper[i,visited]
                



    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.dfsHelper(0,visited)    



