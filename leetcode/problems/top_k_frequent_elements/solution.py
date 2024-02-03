class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        heap = []
        for i, v in freq_map.items():
            if len(heap) == k:
                heappushpop(heap, (v, i))
            else:
                heappush(heap, (v, i))
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1])
        return res

        
