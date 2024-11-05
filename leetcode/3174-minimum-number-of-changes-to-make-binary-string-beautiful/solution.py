class Solution:
    def minChanges(self, s: str) -> int:
        i, count = 0, 0
        while i < len(s):
            if s[i] != s[i + 1]:
                count += 1
            i += 2
        return count


