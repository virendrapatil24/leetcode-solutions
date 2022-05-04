class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        r1 = len(mat)
        c1 = len(mat[0])
        
        if mat == [] or r1*c1 != r*c : return mat
        
        new_mat = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        
        for row in mat:
            for col in row:
                new_mat[k//c][k%c] = col
                k += 1
        
        return new_mat
                
