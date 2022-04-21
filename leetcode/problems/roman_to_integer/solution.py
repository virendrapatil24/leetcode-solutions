class Solution:
    def romanToInt(self, s: str) -> int:     
        value = 0
        
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for x in range(len(s)-1,-1,-1):
            y = roman[s[x]]
            if 4 * y < value: value -= y
            else: value += y
    
        return value