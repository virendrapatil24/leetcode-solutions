class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in ans:
            if s.count(i) != t.count(i): return False
        
        return True