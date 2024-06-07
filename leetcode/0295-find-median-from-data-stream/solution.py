class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, num * -1)

        if self.max_heap and self.min_heap and (self.max_heap[0] * -1 > self.min_heap[0]):
            val = heappop(self.max_heap) * -1
            heappush(self.min_heap, val)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heappop(self.max_heap) * -1
            heappush(self.min_heap, val)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heappop(self.min_heap)
            heappush(self.max_heap, val * -1)
        

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return self.max_heap[0] * -1
        else:
            return (self.min_heap[0] + self.max_heap[0] * -1) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
