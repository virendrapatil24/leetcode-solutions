class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        minHeap, count = heights[:], 0
        heapify(minHeap)
        for i in range(len(heights)):
            if heights[i] != heappop(minHeap):
                count += 1
        return count
        
