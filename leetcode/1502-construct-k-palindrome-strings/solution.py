class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        ones = 0
        for count in freq:
            if count % 2 == 1:
                ones += 1

        return ones <= k
        
        
