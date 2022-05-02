class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxcount = 0
        l = []
        count = 0
        for i in range(len(s)):
            j = i + 1
            for j in range(len(s)+1):
                x = s[i:j]
                if len(set(x)) == 95: return 95
                if len(set(x)) == len(x) and len(set(x)) > maxcount:
                    maxcount = max(len(x), maxcount)
        
        return maxcount