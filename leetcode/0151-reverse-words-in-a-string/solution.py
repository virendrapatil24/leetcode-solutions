class Solution:
    def reverseWords(self, s: str) -> str:
        sSplit = s.split()
        sSplit.reverse()
        return " ".join(sSplit)
        
