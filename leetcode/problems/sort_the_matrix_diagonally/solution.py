class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        d = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        for k in d:
            d[k].sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop(0)
        return mat