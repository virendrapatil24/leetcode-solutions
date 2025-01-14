class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n -1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1  
                elif temp < 0:
                    j += 1
                else:
                    k -= 1
        return triplets
