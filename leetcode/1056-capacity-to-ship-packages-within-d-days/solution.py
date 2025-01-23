class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if self.is_possible(weights, mid, days):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res

    def is_possible(self, weights, capacity, days):
        req_days = 1
        curr_capacity = 0
        for weight in weights:
            if curr_capacity + weight > capacity:
                curr_capacity = weight
                req_days += 1
            else:
                curr_capacity += weight
        return req_days <= days
        
