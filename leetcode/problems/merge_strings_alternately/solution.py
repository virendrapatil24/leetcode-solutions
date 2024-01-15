class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res, i = "", 0
        while i < len(word1):
            if i == len(word2):
                return res + word1[i:]
            res += word1[i] + word2[i]
            i += 1
        return res + word2[i:]
        