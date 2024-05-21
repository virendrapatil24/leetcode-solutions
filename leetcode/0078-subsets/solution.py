class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def create_subsets(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                create_subsets(i + 1, path + [nums[i]])
        res = []
        create_subsets(0, [])
        return res

             
