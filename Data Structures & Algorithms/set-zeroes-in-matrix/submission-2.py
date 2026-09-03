class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #Time - O(m*n) Space - O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     #Time - O(m*n) Space - O(m+n)
    #     ROWS, COLS = len(matrix), len(matrix[0])
    #     rows, cols = [False] * ROWS, [False] * COLS

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if matrix[r][c] == 0:
    #                 rows[r] = True
    #                 cols[c] = True

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if rows[r] or cols[c]:
    #                 matrix[r][c] = 0
        
        