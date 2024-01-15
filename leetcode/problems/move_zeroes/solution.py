class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                j -= 1
            else:
                i += 1

        