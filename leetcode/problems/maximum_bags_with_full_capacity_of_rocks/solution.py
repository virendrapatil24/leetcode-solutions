class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        from collections import Counter
        N = len(rocks)
        bag_full = [0] * N
        
        for i in range(N):
            bag_full[i] = capacity[i] - rocks[i]
        
        if sum(bag_full) <= additionalRocks: return N
        
        x = Counter(bag_full)
        
        l = [i for i in x]
        
        l.sort()
        
        count = x[0]
        
        for i in l:
            if i == 0: continue
            
            if i * x[i] <= additionalRocks:
                additionalRocks -= i * x[i]
                count += x[i]
            else:
                count += additionalRocks // i 
                additionalRocks -= (additionalRocks // i )* i
        return count
            