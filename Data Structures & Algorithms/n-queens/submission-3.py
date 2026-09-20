class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, posDiag, negDiag = set(), set(), set()
        queens = [0] * n
        res = []

        #Space - O(N)
        #Time - O(N!)

        def backtrack(r):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in queens])
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                queens[r] = c
                col.add(c); posDiag.add(r + c); negDiag.add(r - c)
                backtrack(r + 1)
                col.remove(c); posDiag.remove(r + c); negDiag.remove(r - c)

        backtrack(0)
        return res


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:

#         #We need to maintain the Cols of where the QUeen is place
#         #We dont need to track rows, because we go row by row
#         #We need to track cols, PosDiag, NegDiag. We maintain 3 sets to store all info we need

#         #posDiag - r + c stays the same
#         #negDiag - r - c stays the same


#         #Space - O(n^2) for the board, recursion stack is at most n deep o(n)
#         #Time - O(n!)
#         # O(n!) nodes, O(n) work per node, so O(n · n!) upper bound, much lower in practice due to pruning.
#         col = set()
#         posDiag = set() #r+c 
#         negDiag = set() #r-c
#         res = []

#         board = [["."]*n for i in range(n)] #n*n

#         def backtrack(r):
#             if r==n:
#                 copy = ["".join(row) for row in board]
#                 res.append(copy) #For n=4, res has 2 lists stored
#                 return

#             for c in range(n):
#                 if c in col or (r+c) in posDiag or (r-c) in negDiag:
#                     continue
#                 board[r][c] = "Q"
#                 col.add(c)
#                 posDiag.add(r+c)
#                 negDiag.add(r-c)

#                 backtrack(r+1)

#                 board[r][c] = "."
#                 col.remove(c)
#                 posDiag.remove(r+c)
#                 negDiag.remove(r-c)
        
#         backtrack(0)
#         return res



        