class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r, res = 0, x-1, -1
        while l <= r:
            mid = (l + r) // 2
            if x > mid * mid:
                l = mid + 1
                res = mid
            elif x < mid * mid:
                r = mid - 1
            else:
                return mid
        return res

        