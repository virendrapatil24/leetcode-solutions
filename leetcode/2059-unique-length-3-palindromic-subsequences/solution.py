class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_set = set()
        pal_seq = 0
        for l in range(len(s) - 2):
            if s[l] in char_set:
                continue
            char_set.add(s[l])
            m, r = l + 1, len(s) - 1
            between = set()
            while r > m and s[r] != s[l]:
                r -= 1
            while m < r:
                between.add(s[m])
                m += 1
            pal_seq += len(between)      
        return pal_seq


