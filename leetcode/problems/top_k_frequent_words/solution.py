class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_map = {}
        for word in words:
            freq_map[word] = freq_map.get(word, 0) + 1
        heap = []
        for i, v in freq_map.items():
            heappush(heap, (-v, i))
        return [heappop(heap)[1] for _ in range(k)]

        