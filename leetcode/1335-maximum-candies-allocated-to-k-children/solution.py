class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, max(candies)
        min_no_candies = 0
        while l <= r:
            m = (l + r) // 2
            if self.is_possible(candies, k , m):
                min_no_candies = m
                l = m + 1
            else:
                r = m - 1
        return min_no_candies
    
    def is_possible(self, candies, k, m):
        for pile in candies:
            if m == 0:
                return True
            k -= pile // m
            if k <= 0:
                return True
        return False
    
