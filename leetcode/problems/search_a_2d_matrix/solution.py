class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] >= target:
                if target in i: return True
                else: False
        
        return False