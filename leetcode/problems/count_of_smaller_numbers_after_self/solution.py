class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        counts = [0] * len_nums
        tail = [nums[len_nums - 1]]
        for i in range(len_nums - 2, -1, -1):
            idx = bisect_left(tail, nums[i])
            counts[i] = idx
            tail.insert(idx, nums[i])
        return counts
        