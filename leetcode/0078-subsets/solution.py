class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(stack, idx):
            if idx == n:
                res.append(stack[:])
                return 

            stack.append(nums[idx])
            dfs(stack, idx + 1)

            stack.pop()
            dfs(stack, idx + 1)

        dfs([], 0)
        return res

        
