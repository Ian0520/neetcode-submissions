class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)
        row = -1
        while top < bot:
            mid = (bot + top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid
            else:
                row = mid
                break
        if row == -1:
            return False
        
        left = 0
        right = len(matrix[row])
        while left < right:
            mid = (right + left) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid
        return False
