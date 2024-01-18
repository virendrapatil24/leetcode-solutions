class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numsHash = defaultdict(int)
        res = []

        for num in nums:
            numsHash[num] += 1

        n = n // 3
        for k, v in numsHash.items():
            if v > n:
                res.append(k)
        
        return res