class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        visited = [0] * len(nums)
        def rec_per(stack, visited):
            if len(stack) == len(nums):
                res.append(stack[:])
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = 1
                    stack.append(nums[i])
                    rec_per(stack, visited)
                    stack.pop()
                    visited[i] = 0
        rec_per(stack, visited)
        return res
        
