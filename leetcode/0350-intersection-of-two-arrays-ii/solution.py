class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {}
        for num in nums1:
            nums1_map[num] = nums1_map.get(num, 0) + 1
        res = []
        for num in nums2:
            if nums1_map.get(num):
                res.append(num)
                nums1_map[num] -= 1
        return res
        
