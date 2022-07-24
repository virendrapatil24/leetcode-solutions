class Solution:
   def searchMatrix(self, matrix, target: int) -> bool:
        """
        Given a matrix of integers with each row and column
        sorted in ascending order, this program searches for
        a given target value.

        :param matrix: matrix of integers with each row and
                       column sorted in ascending order
        :type matrix: list[list[int]]
        :param target: target value
        :type target: int
        :return: True if target found, else False
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        """
        Start searching the matrix from the first row, last
        column. Continue until the target value is found or
        the search goes off the grid (target not found).
        """
        r = 0
        c = cols - 1
        while matrix[r][c] != target:
            """
            Move down the rows in the same column until we reach
            a value that is greater than or equal to target. Return
            False if we go off the grid.
            """
            while matrix[r][c] < target:
                r += 1
                if r == rows:
                    return False
            """
            Move left in the same row until we reach a value
            that is less than or equal to target. Return False
            if we go off the grid.
            """
            while matrix[r][c] > target:
                c -= 1
                if c < 0:
                    return False
        return True