class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in words:
            if len(i) <= len(s): 
                if i[:len(i)] == s[:len(i)]: count += 1
                    
        return count