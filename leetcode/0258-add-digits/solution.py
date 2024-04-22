class Solution:
    def addDigits(self, num: int) -> int:
        if num >= 10:
            res = num // 10 + num % 10
            if res < 10:
                return res
            else:
                return self.addDigits(res)
        else:
            return num
        
