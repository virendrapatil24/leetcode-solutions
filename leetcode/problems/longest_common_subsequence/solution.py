class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = max(res[i-1][j], res[i][j-1])
        
        return res[len(text1)][len(text2)]