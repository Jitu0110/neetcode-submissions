class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Valid Tree conditions
        #1) No disconnected parts
        #2) Nodes - 1 = edges
        #3) No cycles (1 and 2 automatically satisfy 3)
        visited = [0] * n

        adjList = {i:[] for i in range(n)}

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

        if (0 not in visited) and (n == len(edges)+1):
            return True
        return False
            

        