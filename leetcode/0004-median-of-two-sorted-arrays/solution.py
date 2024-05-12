class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        l, r = 0, m
        while l <= r:
            i1 = (l + r) // 2
            i2 = ((m + n + 1) // 2) - i1

            min_r1 = inf if i1 >= m else nums1[i1]
            max_l1 = -inf if i1 <= 0 else nums1[i1 - 1]

            min_r2 = inf if i2 >= n else nums2[i2]
            max_l2 = -inf if i2 <= 0 else nums2[i2 - 1]

            if max_l2 <= min_r1 and max_l1 <= min_r2:
                if (m + n) % 2 == 0:
                    return (max(max_l1, max_l2) + min(min_r1, min_r2)) / 2
                else:
                    return max(max_l1, max_l2)
            elif max_l1 > min_r2:
                r = i1 - 1
            else:
                l = i1 + 1
            

            
        
