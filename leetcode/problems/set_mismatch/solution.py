class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = (n*(n+1))//2
        numMiss = s - sum(set(nums))
        numTwice = sum(nums) - s + numMiss
        
        return [numTwice, numMiss]