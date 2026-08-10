class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        # visit = set() use set if we cannot modify the grid. vist.add(r,c) and check if (r,c) in visited in DFS
        def dfs(r,c):
            if(r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]==0):
                return 0
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1))

        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 0
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    #area = dfs(i,j)
                    area = bfs(i,j)
                    maxArea = max(maxArea,area)
        
        return maxArea

        