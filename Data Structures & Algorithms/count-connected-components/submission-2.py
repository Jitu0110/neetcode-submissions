class Solution:

    #Time - O(V+E)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        components = 0

        #Time - O(V)
        adjList = {i:[] for i in range(n)}

        #Time - O(E)
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        
        visited = [False]*n

        def dfs(node):
            if visited[node]:
                return

            visited[node] = True

            for neighbors in adjList[node]:
                 dfs(neighbors)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        
        return components




