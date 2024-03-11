class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        s_set = {}
        for char in s:
            s_set[char] = s_set.get(char, 0) + 1
        for char in order:
            if char in s_set:
                res += char * s_set[char]
        for char in s:
            if char not in res:
                res += char * s_set[char]
        return res

        
