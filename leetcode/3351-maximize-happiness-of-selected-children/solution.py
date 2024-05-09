class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        for val in happiness:
            heappush(heap, -val)
        
        happy = heappop(heap) * -1
        for i in range(1, k):
            val = heappop(heap) * -1
            if val > i:
                happy += val - i
        return happy



        
