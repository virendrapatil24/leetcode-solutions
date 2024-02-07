class Solution:
    def frequencySort(self, s: str) -> str:
        map_freq = {}
        for char in s:
            map_freq[char] = map_freq.get(char, 0) + 1
        heap = [(-v, k) for k, v in map_freq.items()]
        heapify(heap)
        res = ""
        while heap:
            v, k = heappop(heap)
            res += -v * k
        return res        

        