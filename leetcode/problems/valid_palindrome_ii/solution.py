class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 0
        while r > l:
            if s[l] != s[r]:
                string1 = s[l:r]
                string2 = s[l+1:r+1]
                return string1 == string1[::-1] or string2 == string2[::-1] 
            else:
                l += 1
                r -= 1
        return True

        