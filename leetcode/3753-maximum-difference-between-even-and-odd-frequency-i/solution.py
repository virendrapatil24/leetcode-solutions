class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord("a")] += 1

        even_freq = inf
        odd_freq = 0
        for fq in freq:
            if fq % 2 == 0:
                if fq != 0:
                    even_freq = min(even_freq, fq) 
            else:
                odd_freq = max(odd_freq, fq)
        # print(odd_freq, even_freq)

        return odd_freq - even_freq
        
