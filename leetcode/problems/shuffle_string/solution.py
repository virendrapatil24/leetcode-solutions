class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        l = []
        for i in range (len(s)):
            d[indices[i]] = s[i]
        for i in range (len(s)):
            l.append(d[i])
        return ''.join(l)