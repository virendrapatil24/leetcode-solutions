class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0,len(nums),2):
            l = [nums[i+1]]
            freq = nums[i]
            res.extend(l*freq)
        return res
        