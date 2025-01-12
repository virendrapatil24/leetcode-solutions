class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp = []
            for j in range(i + 1):
                if j in [0, i]:
                    temp.append(1)
                else:
                    temp.append(res[-1][j] + res[-1][j - 1])
            res.append(temp)
        return res

        
