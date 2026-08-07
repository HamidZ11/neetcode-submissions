class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols) - 1
        while left <= right:
            middle = (left + right) // 2
            row = middle // cols
            col = middle % cols
            if target > matrix[row][col]:
                left = middle + 1
            elif target < matrix[row][col]:
                right = middle - 1
            else: 
                return True
        
        return False