class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, min(ranks) * cars * cars
        while l <= r:
            m = (l + r) // 2
            if self.is_possible(ranks, cars, m):
                r = m - 1
            else:
                l = m + 1
        return l
    
    def is_possible(self, ranks, cars, m):
        count = 0
        for rank in ranks:
            count += int(((m / rank) ** 0.5))
        return count >= cars

        
