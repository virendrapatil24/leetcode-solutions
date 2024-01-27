class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2: return None

        res, mapping, stack = [], {}, [nums2[0]]

        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapping[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        for num in stack:
            mapping[num] = -1
        
        for num in nums1:
            res.append(mapping[num])

        return res
            
            
        