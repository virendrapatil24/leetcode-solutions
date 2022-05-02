class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        leven = []
        lodd = []
        for i in nums:
            if  i % 2 == 0: leven.append(i)
            else: lodd.append(i)
        return leven+lodd
            