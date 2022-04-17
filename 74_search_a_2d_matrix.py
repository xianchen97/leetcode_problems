class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Calculate number of rows and columns
        ROW, COLS = len(matrix), len(matrix[0])
        
        top, bottom = 0, ROW-1
        # Navigate to each column and find the correct row
        while top <= bottom:
            row = (top + bottom)//2
            if matrix[row][0] > target:
                bottom = row-1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        l, r = 0, COLS-1
        row = (top + bottom) // 2
        
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] > target:
                r = mid-1
            elif matrix[row][mid] < target:
                l = mid+1
            else:
                return True
        return False
        
        
        