class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ele, freq = nums[0], 1
        for i in range(1, n):
            if freq != 0:
                freq += 1 if nums[i] == ele else -1
            else:
                ele, freq = nums[i], 1
        
        count = 0
        for num in nums:
            if num == ele:
                count += 1

        # print(ele, count, n // 2 + 1)
        if count - (n - count) < 2:
            return -1
        
        non_dom, dom = 0, 0
        for i, num in enumerate(nums):
            if num == ele:
                dom += 1
            else:
                non_dom += 1
            
            if dom > non_dom:
                break
        
        return i
        
