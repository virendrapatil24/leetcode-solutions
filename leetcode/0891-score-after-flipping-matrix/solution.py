class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row_len = len(grid[0])
        col_len = len(grid)

        def flip_row(row_idx, grid):
            for i in range(row_len):
                grid[row_idx][i] = grid[row_idx][i] ^ 1
        
        def flip_col(col_idx, grid):
            for i in range(col_len):
                grid[i][col_idx] = grid[i][col_idx] ^ 1

        for i in range(col_len):
            if grid[i][0] == 0:
                flip_row(i, grid)
        
        col_cnt_one = []
        for i in range(row_len):
            temp = 0
            for j in range(col_len):
                if grid[j][i] == 1:
                    temp += 1
            col_cnt_one.append(temp)

        for i in range(row_len):
            if col_cnt_one[i] <= col_len // 2:
                flip_col(i, grid)

        score = 0
        for col in grid:
            score += int("".join(map(str, col)), 2)

        return score
        
