class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def dfs(curr_sum, stack, idx):
            if curr_sum == target:
                res.append(stack[:])
                return
            
            if curr_sum > target or idx >= n:
                return
            
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                stack.append(candidates[i])
                curr_sum += candidates[i]
                dfs(curr_sum, stack, i + 1)
                curr_sum -= candidates[i]
                stack.pop()
        
        dfs(0, [], 0)
        return res
        
