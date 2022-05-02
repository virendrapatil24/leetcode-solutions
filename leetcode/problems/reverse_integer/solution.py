class Solution:
    def reverse(self, x: int) -> int:
        y =  str(x)
        if y[0] == '-':
            a = '-' + y[:0:-1]
        else:
            a = y[::-1]
        
        b = int(a)
        
        if -2 ** 31 < b  and b < 2 ** 31 - 1:
            return b
        else: return 0

            