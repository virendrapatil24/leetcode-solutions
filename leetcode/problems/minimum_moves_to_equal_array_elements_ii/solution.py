class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        med = sorted(nums)[len(nums)//2]
        res = 0
        for num in nums:
            res += abs(med - num)
        return res
        