class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        neg_occr = self.getOccurence(nums, True)
        pos_occr = self.getOccurence(nums, False)
        if neg_occr == -1 and pos_occr == -1:
            return 0
        if neg_occr == -1:
            return n - pos_occr
        if pos_occr == -1:
            return neg_occr + 1
        return max(neg_occr + 1, n - pos_occr)
    
    def getOccurence(self, nums, is_neg):
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < 0:
                if is_neg:
                    idx = m
                l = m + 1
            elif nums[m] > 0:
                if not is_neg:
                    idx = m
                r = m - 1
            else:
                if is_neg:
                    r = m - 1
                else:
                    l = m + 1
        return idx
                
            


        
