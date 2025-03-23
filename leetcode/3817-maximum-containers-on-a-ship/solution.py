class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cells = n * n
        max_containers = maxWeight // w
        return min(cells, max_containers)
            
        
        
