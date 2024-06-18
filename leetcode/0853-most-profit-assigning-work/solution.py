class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        map_diff_profit = [(d, p/d) for d, p in zip(difficulty, profit)]
        map_diff_profit.sort()
        worker.sort()
        total_profit = 0
        max_heap = []
        i = 0
        for w in worker:
            while i < len(profit) and map_diff_profit[i][0] <= w:
                heappush(max_heap, (-1 * map_diff_profit[i][1] * map_diff_profit[i][0]))
                i += 1
            if max_heap:
                total_profit -= max_heap[0]
        return int(total_profit)
        
