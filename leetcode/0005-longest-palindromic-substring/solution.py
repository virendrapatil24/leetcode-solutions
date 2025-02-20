class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                new_s = s[i:j + 1]
                is_palindrome = self.is_palindrome(new_s)
                if is_palindrome and len(new_s) > len(res):
                    res = new_s
        return res

    def is_palindrome(self, s):
        return s == s[::-1]
        
