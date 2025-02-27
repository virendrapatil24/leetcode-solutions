class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] =  freq.get(s[j], 0) + 1
                beauty = max(freq.values()) - min(freq.values())
                total_beauty += beauty
        return total_beauty
        
