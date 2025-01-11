class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        cols, rows = [0] * m, [0] * n
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    cols[j] = 1
                    rows[i] = 1
        
        for i in range(n):
            for j in range(m):
                if cols[j] or rows[i]:
                    matrix[i][j] = 0
        

