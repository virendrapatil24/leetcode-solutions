class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def create_subsets(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                create_subsets(i + 1, path)
                path.pop()
        res = []
        create_subsets(0, [])
        return res

             
