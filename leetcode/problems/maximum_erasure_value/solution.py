class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        sub_arr = set()
        curr_sum = 0
        res = 0
        
        for r in range(len(nums)):
            while nums[r] in sub_arr:
                sub_arr.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            sub_arr.add(nums[r])
            curr_sum += nums[r]
            res = max(res, curr_sum)
        
        return res
                