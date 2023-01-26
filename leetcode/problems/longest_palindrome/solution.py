class Solution:
    def longestPalindrome(self, s: str) -> int:
        e, o = 0, 0
        for char in set(s):
            if s.count(char) % 2 == 0:
                e += s.count(char) 
            else:
                e += s.count(char) - 1
                o = 1
        return e+o