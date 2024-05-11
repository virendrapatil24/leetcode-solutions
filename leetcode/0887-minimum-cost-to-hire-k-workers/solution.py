class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        qlty_ratio = sorted([(w/q, q) for w, q in zip(wage, quality)])
        max_heap = []
        max_ratio = 0.0
        qlty_sum = 0
        for i in range(k):
            max_ratio = max(max_ratio, qlty_ratio[i][0])
            qlty_sum += qlty_ratio[i][1]
            heappush(max_heap, -qlty_ratio[i][1])
        
        min_cost = max_ratio * qlty_sum
        for i in range(k, len(qlty_ratio)):
            max_ratio = max(max_ratio, qlty_ratio[i][0])
            qlty_sum += qlty_ratio[i][1] + heappop(max_heap)
            min_cost = min(min_cost, qlty_sum * max_ratio)
            heappush(max_heap, -qlty_ratio[i][1])
        
        return min_cost


