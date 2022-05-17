class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        self.dfs(candidates, target, [], final)
        return final
    
    def dfs(self, nums, target, path, final):
        if target < 0:
            return
        
        if target == 0:
            final.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], final)
              
        