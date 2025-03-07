class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def create_subset(idx, temp):
            res.append(temp)
            for i in range(idx, len(nums)):
                create_subset(i + 1, temp + [nums[i]])
        create_subset(0, [])
        return res

        
