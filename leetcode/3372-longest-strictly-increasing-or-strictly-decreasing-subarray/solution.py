class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_in, curr_in = 1, 1
        max_dec, curr_dec = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_in += 1
                max_dec = max(max_dec, curr_dec)
                curr_dec = 1
            elif nums[i] < nums[i - 1]:
                curr_dec += 1
                max_in = max(max_in, curr_in)
                curr_in = 1
            else:
                max_dec = max(max_dec, curr_dec)
                max_in = max(max_in, curr_in)
                curr_dec, curr_in = 1, 1
        return max(max_dec, max_in, curr_in, curr_dec)
