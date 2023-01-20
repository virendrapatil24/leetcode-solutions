class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        for num in nums:
            for i in str(num):
                digit_sum += int(i)
        return abs(sum(nums) - digit_sum)
