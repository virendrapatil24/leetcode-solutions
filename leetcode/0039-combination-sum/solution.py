class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.generate_combinations(candidates, target, 0, [], 0, [])

    def generate_combinations(self, candidates, target, curr_sum, stack, i, res):
        if curr_sum == target:
            res.append(stack[:])
            return

        if curr_sum >= target:
            return
        
        if i >= len(candidates):
            return

        stack.append(candidates[i])
        curr_sum += candidates[i]
        self.generate_combinations(candidates, target, curr_sum, stack, i, res)
        curr_sum -= candidates[i]
        stack.pop()

        self.generate_combinations(candidates, target, curr_sum, stack, i + 1, res)
        return res


        
