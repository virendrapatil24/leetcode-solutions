class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        while len(nums) > 1:
            new_nums = [0] * (len(nums) // 2)
            for i in range(0, (len(nums) // 2)):
                if i % 2 == 0:
                    new_nums[i] = min(nums[2*i], nums[2*i+1])
                else:
                    new_nums[i] = max(nums[2*i], nums[2*i+1])
            nums = new_nums
        
        return nums[0]
        
