class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from copy import deepcopy
        

        #check for row
        a_board = deepcopy(board)
        for i in a_board:
            while '.' in i: i.remove('.')
            if len(set(i)) != len(i): return False
        
        #check for column
        b_board = deepcopy(board)
        col_board = []
        for a in range(9):
            temp = []
            for b in range(9):
                temp.append(b_board[b][a])
            col_board.append(temp)
        for i in col_board:
            while '.' in i: i.remove('.')
            if len(set(i)) != len(i): return False
        
        #check for 3x3 box
        c_board = deepcopy(board)
        box_board = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                l = []
                for m in range(i,i+3):
                    for n in range(j,j+3):
                        l.append(c_board[m][n])
                box_board.append(l)
        for i in box_board:
            while '.' in i: i.remove('.')
            if len(set(i)) != len(i): return False
            

        
        return True
        
                
            