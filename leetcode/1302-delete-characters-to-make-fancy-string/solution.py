class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for char in s:
            if len(res) > 1 and char == res[-1] == res[-2]:
                continue
            res += char
        return res
