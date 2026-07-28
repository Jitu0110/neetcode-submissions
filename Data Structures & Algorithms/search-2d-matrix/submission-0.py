class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row,col = len(matrix), len(matrix[0])
        left = 0
        right = row*col - 1

        while left <= right:
            mid = left + (right - left)//2 #One Dimension Mid

            row_iter = mid // col #2D Mid index (x)
            col_iter = mid % col #2D Mid index (y)

            if matrix[row_iter][col_iter] == target:
                return True
            elif matrix[row_iter][col_iter] > target:
                right = mid - 1
            elif matrix[row_iter][col_iter] < target:
                left = mid + 1
        
        return False


      


