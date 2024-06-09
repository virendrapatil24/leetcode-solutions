class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashMap = {0 : 1}
        prefixSum = 0
        res = 0
        for num in nums:
            prefixSum += num
            remainder = prefixSum % k
            # if remainder < 0:
            #     remainder += k
            if remainder in hashMap:
                res += hashMap[remainder]
            hashMap[remainder] = hashMap.get(remainder, 0) + 1
        return res
                


        
