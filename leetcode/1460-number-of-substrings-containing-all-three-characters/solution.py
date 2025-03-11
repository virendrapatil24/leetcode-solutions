class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_map = {}
        count = 0
        l = 0
        for r in range(len(s)):
            char_map[s[r]] = char_map.get(s[r], 0) + 1
            while len(char_map) == 3:
                count += len(s) - r
                char_map[s[l]] -= 1
                if char_map[s[l]] == 0:
                    char_map.pop(s[l])
                l += 1
        return count
        
