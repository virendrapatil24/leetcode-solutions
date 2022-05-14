class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        i = 0
        count = 0
        while i <= (len(s) - k):
            x = s[i:k+i]
            if int(x) == 0: 
                i += 1
                continue
            if num % int(x) == 0: count += 1
            i += 1
        return count