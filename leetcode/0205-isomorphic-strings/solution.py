class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        used = set()
        for i in range(len(s)):
            if s[i] in char_map and char_map[s[i]] != t[i]:
                return False
            if s[i] not in char_map and t[i] in used:
                return False
            char_map[s[i]] = t[i]
            used.add(t[i])
        return True
        
