class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_count = [0] * 26
        t_count = [0] * 26
        
        for char in s:
            s_count[ord(char) - ord("a")] += 1
        
        for char in t:
            t_count[ord(char) - ord("a")] += 1

        for i in range(26):
            if s_count[i] != t_count[i]:
                return False
        
        return True
        
        
