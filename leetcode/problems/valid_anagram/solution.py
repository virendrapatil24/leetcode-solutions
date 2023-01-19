class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in set(s):
            if len(s) != len(t) or s.count(char) != t.count(char):
                return False
        return True