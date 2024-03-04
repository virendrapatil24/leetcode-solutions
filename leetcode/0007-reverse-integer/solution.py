class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: res = -int(str(x)[-1:0:-1])
        else: res = int(str(x)[::-1])
        return res if -2 ** 31 < res  and res < 2 ** 31 - 1 else 0

        
