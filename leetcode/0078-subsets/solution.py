class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        len_subsets = 1 << len(nums)
        for i in range(len_subsets):
            curr_subset = []
            for j in range(len(nums)):
                if i & (1 << j) > 0:
                    curr_subset.append(nums[j])
            subsets.append(curr_subset)
        return subsets

        
