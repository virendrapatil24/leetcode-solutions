class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map_count = {}
        for word in words:
            map_count[word] = map_count.get(word, 0) + 1
        heap = []
        for key, val in map_count.items():
            heappush(heap, (-val, key))
        return [heappop(heap)[1] for _ in range(k)]

