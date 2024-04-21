class Solution:
    def reverse(self, x: int) -> int:
        def reverse_num(pos_num):
            rev = 0
            while pos_num > 0:
                rev = rev * 10 + pos_num % 10
                pos_num //= 10
            return rev
        if x < 0:
            res = reverse_num(x * -1) * -1
        else:
            res = reverse_num(x)
        return res if -2 ** 31 < res and res < 2 ** 31 - 1 else 0

        
