class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def create_subsets(start, path):
            res.add(tuple(path[:]))
            for i in range(start, len(nums)):
                path.append(nums[i])
                create_subsets(i+1, path)
                path.pop()
        create_subsets(0, [])
        return res
        
