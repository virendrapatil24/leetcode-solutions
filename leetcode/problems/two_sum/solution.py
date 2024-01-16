class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            if nums[i] not in numMap.keys():
                numMap[target-nums[i]] = i
            else:
                return [numMap[nums[i]], i]

        