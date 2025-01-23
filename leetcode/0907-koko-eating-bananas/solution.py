class Solution: 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ele = max(piles)
        res = inf
        l, r = 1, max_ele
        while l <= r:
            m = (l + r) // 2
            total_hrs = self.get_hrs(piles, m)

            if total_hrs <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
    
    def get_hrs(self, piles, hi):
        hrs = 0
        for pile in piles:
            hrs += (pile + hi - 1) // hi
        return hrs
