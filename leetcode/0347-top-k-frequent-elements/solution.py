class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_count = {}
        for num in nums:
            map_count[num] = map_count.get(num, 0) + 1
        heap = []
        for key, val in map_count.items():
            if len(heap) >= k:
                heappushpop(heap, (val, key))
            else:
                heappush(heap, (val, key))
        res = []
        for i in range(k):
            res.append(heappop(heap)[1])
        return res
        
