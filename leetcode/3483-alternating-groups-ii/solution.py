class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        l = 0
        count = 0
        for r in range(1, n + k - 1):
            if colors[r % n] == colors[(r - 1) % n]:
                l = r
            
            if r - l + 1 > k:
                l += 1
            
            if r - l + 1 == k:
                count += 1
        
        return count
