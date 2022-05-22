class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        for i in range(N):
            for j in range(i, N):
                x = s[i:j+1]
                if s[i:j+1] == x[::-1]: res += 1
        return res