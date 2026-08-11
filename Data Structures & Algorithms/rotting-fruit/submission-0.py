class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0
        countOfFreshFruits= 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    countOfFreshFruits += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        
        while q and countOfFreshFruits > 0:
            time += 1
            for _ in range(len(q)):
                row,col = q.popleft()

                for dx,dy in directions:
                    newRow = row + dx
                    newCol = col + dy

                    if(newRow<0 or newRow>=ROWS or newCol<0 or newCol>=COLS or grid[newRow][newCol]!=1 ):
                        continue
                    grid[newRow][newCol] = 2
                    q.append([newRow,newCol])
                    countOfFreshFruits -= 1
        
        return time if (countOfFreshFruits==0) else -1
        



 



        