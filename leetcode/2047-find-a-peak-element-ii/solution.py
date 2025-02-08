class Solution:
    def findPeakGrid(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, COLS - 1

        def get_max_row(matrix, col):
            max_ele_idx = 0 
            for i in range(ROWS):
                if matrix[i][col] > matrix[max_ele_idx][col]:
                    max_ele_idx = i
            return max_ele_idx
        
        while l <= r:
            mid = (l + r) // 2
            row = get_max_row(matrix, mid)
            left = matrix[row][mid - 1] if mid > 0 else -1
            right = matrix[row][mid + 1] if mid < COLS - 1 else -1
            if left < matrix[row][mid] > right:
                return [row, mid]
            elif left > matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
        
