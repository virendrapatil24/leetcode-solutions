class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(stack, idx, curr_sum):
            if len(stack) == k and curr_sum == n:
                res.append(stack[:])
                return
            
            if curr_sum > n or len(stack) > k:
                return
            
            for i in range(idx, 10):
                stack.append(i)
                dfs(stack, i + 1, curr_sum + i)
                stack.pop()
        
        dfs([], 1, 0)
        return res
        
