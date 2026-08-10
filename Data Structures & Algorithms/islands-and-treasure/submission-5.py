from collections import deque

class Solution:

    #Time - O(ROW * COL)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

#First, we iterate through the grid and add positions of Treasure Chest in a queue(BFS)
#Then we do BFS and iterate. If we reach water or treasure chest, immediately return. If we reach land, update it with 'distance'. So we need to keep a track of distance traversed
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i,j])

        def bfs():
            distance = 0
            while q:
                distance += 1
                for _ in range(len(q)):
                    row,col = q.popleft()

                    for dx,dy in directions:
                        newRow, newCol = row + dx, col + dy

                        if newRow<0 or newCol <0 or newRow >=ROWS or newCol >= COLS or grid[newRow][newCol] != INF:
                            continue
                        q.append([newRow,newCol])
                        grid[newRow][newCol] = distance
        
        bfs()

        return None


            
                    
                    
                     





     
        