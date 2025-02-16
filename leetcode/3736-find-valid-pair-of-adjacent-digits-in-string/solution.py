class Solution:
    def findValidPair(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i in range(1, len(s)):
            first_freq = freq.get(s[i - 1])
            second_freq = freq[s[i]]
            if s[i - 1] != s[i] and first_freq == int(s[i - 1]) and second_freq == int(s[i]):
                return s[i - 1] + s[i]

        return ""
        
