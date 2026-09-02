class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Time (O(M*N))
        #Space (O(M*N))

        result = []
        ROWS, COLS = len(heights), len(heights[0])
        
        pacificVisited = [[False] * COLS for _ in range(ROWS)]
        atlanticVisited = [[False] * COLS for _ in range(ROWS)]

        #pacificVisited = atlanticVisited = [[False] * COLS for _ in range(ROWS)]


        def dfs(visited,i,j,prevHeight):
            if i<0 or i>=ROWS or j<0 or j>=COLS or visited[i][j] or heights[i][j] < prevHeight:
                return
            visited[i][j] = True

            dfs(visited,i+1,j,heights[i][j] )
            dfs(visited,i,j+1,heights[i][j] )
            dfs(visited,i-1,j,heights[i][j] )
            dfs(visited,i,j-1,heights[i][j] )
        
        def bfs(visited,i,j):
            q = deque()
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            q.append([i,j])
            visited[i][j] = True

            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    newRow = dr + r
                    newCol = dc + c
                    
                    if newRow<0 or newRow>=ROWS or newCol<0 or newCol>=COLS or visited[newRow][newCol] or heights[newRow][newCol] < heights[r][c]:
                        continue
                    q.append([newRow,newCol])
                    visited[newRow][newCol] = True
                    


        
        #North
        for i in range(COLS):
            bfs(pacificVisited, 0,i)


        #East
        for i in range(ROWS):
            bfs(atlanticVisited,i,COLS-1)


        #South
        for i in range(COLS):
            bfs(atlanticVisited,ROWS-1,i)


        #West
        for i in range(ROWS):
            bfs(pacificVisited,i,0)

        
        for i in range(ROWS):
            for j in range(COLS):
                if pacificVisited[i][j] and atlanticVisited[i][j]:
                    result.append([i,j])
        
        return result


