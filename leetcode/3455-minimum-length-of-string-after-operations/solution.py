class Solution:
    def minimumLength(self, s: str) -> int:
        s_freq = [0] * 26
        for char in s:
            s_freq[ord(char) - ord('a')] += 1
        
        min_len = 0
        for freq in s_freq:
            if freq == 0:
                continue
            elif freq % 2 == 0:
                min_len += 2
            else:
                min_len += 1
        return min_len
