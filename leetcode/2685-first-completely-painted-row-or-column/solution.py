class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        hash_map = {}
        for i in range(m):
            for j in range(n):
                hash_map[mat[i][j]] = (i, j)
        rows = [0] * m
        cols = [0] * n
        for i in range(len(arr)):
            r, c = hash_map[arr[i]]
            rows[r] += 1
            cols[c] += 1
            # print(rows, cols)
            if rows[r] == n or cols[c] == m:
                return i

        return -1
        
