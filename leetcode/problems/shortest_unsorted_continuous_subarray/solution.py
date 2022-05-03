class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        from copy import deepcopy
        sorted_nums = deepcopy(nums)
        sorted_nums.sort()
        
        if nums == sorted_nums: return 0
        
        f_occ = 0
        last_occurence = 0
        
        for i  in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if(f_occ < 1):
                    first_occurence = i
                    f_occ += 1
                else:
                    last_occurence = max(last_occurence, i)
        
        output = last_occurence - first_occurence + 1
        
        return output