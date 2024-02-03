class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        map_idx, res = {}, -1
        for i in range(len(s)):
            if s[i] in map_idx:   
                res = max(res, i - map_idx[s[i]] - 1)
            else:
                map_idx[s[i]] = i
        return res

        