class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        res = set()
        for num in nums2:
            if num in nums1_set:
                res.add(num)
        return list(res)
        
