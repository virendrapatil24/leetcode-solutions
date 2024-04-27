class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        map_count = {}
        for num in arr:
            map_count[num] = map_count.get(num, 0) + 1
        heap = list(map_count.values())
        heapify(heap)
        while k > 0:
            val = heappop(heap)
            k -= val
        return len(heap) if k == 0 else len(heap) + 1
