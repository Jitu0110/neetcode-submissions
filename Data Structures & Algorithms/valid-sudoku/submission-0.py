class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Box index - (r // 3) * 3 + (c // 3)

        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue
                
                boxIndex = (i // 3) * 3 + (j // 3)
                if (board[i][j] in rowSet[i] 
                or board[i][j] in colSet[j] 
                or board[i][j] in boxSet[boxIndex]):
                    return False
                
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                boxSet[boxIndex].add(board[i][j])
        
        return True


        