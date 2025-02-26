class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_min_sum = inf
        curr_max_sum = -inf
        res = -inf
        for num in nums:
            curr_min_sum = min(curr_min_sum + num, num)
            curr_max_sum = max(curr_max_sum + num, num)
            res = max(res, curr_max_sum, abs(curr_min_sum))
        return res


        
