class Solution(object):
    def twoSum(self, nums, target):
        anslist = []
        x = 0
        while x <len(nums):
            y = x +1
            while y <len(nums):
                if nums[x] + nums[y] == target:
                    anslist.append(x)
                    anslist.append(y)
                y += 1
            x += 1
        return anslist
        