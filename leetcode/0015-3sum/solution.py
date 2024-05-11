class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif temp > 0:
                    k -= 1
                else:
                    j += 1
        return triplets


        


        
