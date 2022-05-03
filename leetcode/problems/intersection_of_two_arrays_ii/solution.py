class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        from copy import deepcopy
        if(len(nums1) < len(nums2)): nums3 = deepcopy(nums1)
        else: nums3 = deepcopy(nums2)
        
        l = []
        
        for i in nums3:
            if (i in nums2) and (i in nums1):
                l.append(i)
                nums2.remove(i)
                nums1.remove(i)
            else: pass
        
        return l
        
    
    