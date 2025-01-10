class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec_per(i, j):
            if i == j == len(nums):
                res.append(nums[:])
                # return
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                rec_per(i, j)
                i -= 1
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
        rec_per(0, 0)
        return res
