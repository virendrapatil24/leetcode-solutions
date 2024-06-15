class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = list(zip(capital, profits))
        heapify(minHeap)
        maxHeap = []
        for _ in range(min(k, len(profits))):
            while minHeap and minHeap[0][0] <= w:
                profit =  heappop(minHeap)[1]
                heappush(maxHeap, -profit)

            if maxHeap:
                w -= heappop(maxHeap)
            else:
                break

        return w
        
