class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        components = 0

        adjList = {i:[] for i in range(n)}

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




