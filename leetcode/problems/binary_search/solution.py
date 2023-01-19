class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            mid = (rp + lp) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                rp = mid - 1
            else:
                lp = mid + 1
        return -1
