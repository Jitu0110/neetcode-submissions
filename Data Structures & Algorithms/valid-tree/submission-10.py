class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Valid Tree conditions
        #1) No disconnected parts
        #2) Nodes - 1 = edges
        #3) No cycles (1 and 2 automatically satisfy 3)
        if n == 0:
            return False

        if n != len(edges)+1: #Number of Edges = number of nodes - 1
            return False

        visited = [0] * n

        adjList = {i:[] for i in range(n)}

        #Adjlist for the edges, un-directed
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        def dfs(node):
            if visited[node] == 1:
                return

            visited[node] = 1

            for neighbors in adjList[node]:
                 dfs(neighbors)


        dfs(0) 

        if sum(visited)==n:
            return True
        return False
            

        