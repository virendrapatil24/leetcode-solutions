class Solution:
    def reverse(self, x: int) -> int:
        def reverse_num(num):
            rev = 0
            while num > 0:
                rev = rev * 10 + num % 10
                num //= 10
            return rev
        res = 0
        if x < 0:
            res = reverse_num(x * -1) * -1
        else:
            res = reverse_num(x)
        
        return res if -2**31 < res < 2**31 - 1 else 0
        
