class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        def dfs(stack, idx):
            res.append(stack[:])
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                stack.append(nums[i])
                dfs(stack, i + 1)
                stack.pop()
        
        dfs([], 0)
        return res

        
