class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3, c // 3)].add(num)
        
        def backtrack(idx):
            if idx == len(empty_cells):
                return True
            
            r, c = empty_cells[idx]
            for num in "123456789":
                if (num not in rows[r] and 
                    num not in cols[c] and
                    num not in boxes[(r // 3, c // 3)]):
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3, c // 3)].add(num)

                    if backtrack(idx + 1):
                        return True
                    
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[(r // 3, c // 3)].remove(num)
            return False

        return backtrack(0)
                    


        
