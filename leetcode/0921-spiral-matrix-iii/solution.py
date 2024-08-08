class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total, cnt, step, i = rows * cols, 1, 1, 0
        ans = [[rStart, cStart]]
        direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)} # setup direction movements
        while cnt < total:
            for k in range(step):
                rStart, cStart = rStart+direction[i][0], cStart + direction[i][1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                    cnt += 1       # count visited 
            i = (i + 1) % 4        # changing direction
            step += not i % 2      # increase step every 2 directions
        return ans
