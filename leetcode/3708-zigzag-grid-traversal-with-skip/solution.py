class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        zigzag_grid = []
        for i, row in enumerate(grid):
            if i % 2 == 0:
                zigzag_grid.extend(row)
            else:
                zigzag_grid.extend(row[::-1])
        return [num for i, num in enumerate(zigzag_grid) if i % 2 == 0]
        
