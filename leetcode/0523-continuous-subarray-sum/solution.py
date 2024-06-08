class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = 0
        hashMap = {0: -1}
        for idx in range(len(nums)):
            prefixSum += nums[idx]
            remainder = prefixSum % k
            if remainder in hashMap:
                if idx - hashMap[remainder] > 1:
                    return True
            else:
                hashMap[remainder] = idx
        return False
                
