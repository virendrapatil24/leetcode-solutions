class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        l, r = min(bloomDay), max(bloomDay)
        res = max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            bouquets = self.is_valid(bloomDay, mid, m, k)
            if bouquets >= m:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def is_valid(self, bloomDay, min_day, m, k):
        bouquets = 0
        adj_flowers = 0
        for day in bloomDay:
            if min_day >= day:
                adj_flowers += 1
                if adj_flowers == k:
                    bouquets += 1
                    adj_flowers = 0
            else:
                adj_flowers = 0
        # print(min_day, bouquets)
        return bouquets




        
