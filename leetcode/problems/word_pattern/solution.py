class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)):
            return False
        patternMap = {}
        for i in range(len(s)):
            if pattern[i] in patternMap and patternMap[pattern[i]] != s[i]:

                return False
            else:
                patternMap[pattern[i]] = s[i]
        return True
            
        