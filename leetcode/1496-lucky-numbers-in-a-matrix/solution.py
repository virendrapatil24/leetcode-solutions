class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        
        row_min = []
        for i in range(n):
            r_min = inf
            for j in range(m):
                r_min = min(r_min, matrix[i][j])
            row_min.append(r_min)
        
        col_max = []
        for i in range(m):
            c_max = -inf
            for j in range(n):
                c_max = max(c_max, matrix[j][i])
            col_max.append(c_max)
        
        lucky_nums = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    lucky_nums.append(matrix[i][j])
        
        return lucky_nums
        
