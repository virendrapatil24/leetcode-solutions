class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.countReversePairs(nums, 0, len(nums) - 1)
    
    def countReversePairs(self, nums, l, r):
        res = 0
        if r > l:
            m = (l + r) // 2
            res += self.countReversePairs(nums, l, m)
            res += self.countReversePairs(nums, m + 1, r)
            res += self.mergeCount(nums, l, m, r)
        return res
    
    def mergeCount(self, nums, l, m, r):
        left = nums[l: m + 1]
        right = nums[m + 1: r + 1]

        ip, jp, res = 0, 0, 0
        for num in left:
            while jp < len(right) and num > right[jp] * 2:
                jp += 1
            res += jp

        i, j, k = 0, 0, l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                k += 1
                i += 1
            else:
                nums[k] = right[j]
                k += 1
                j += 1
        
        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1

        
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1
        
        return res
        
                

