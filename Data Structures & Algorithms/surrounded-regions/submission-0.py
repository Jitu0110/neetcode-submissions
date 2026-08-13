class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])

        #O(M*N)
        def dfs(x,y):
            if x<0 or x>=ROWS or y<0 or y>=COLS or board[x][y] != 'O':
                return
            board[x][y] = 'Y' #Temp value Y

            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        #O(M*N)
        for i in range(ROWS):
            for j in range(COLS):
                if (i==0 or i==ROWS-1 or j==0 or j==COLS-1) and board[i][j] == 'O':
                    dfs(i,j)



        #O(M*N)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'


        
        
        