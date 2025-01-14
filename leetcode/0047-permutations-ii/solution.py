class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def rec_per(i, j):
            if i == j == len(nums):
                res.add(tuple(nums[:]))
            
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                rec_per(i, j)
                i -= 1
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
        
        rec_per(0, 0)
        return list(res)
        
