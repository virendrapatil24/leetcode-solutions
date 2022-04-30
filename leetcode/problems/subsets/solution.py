class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        if  n == 0: return output
        
        for i in range(pow(2,n)):
            l = []
            for j in range(n):
                if i & (1 << j) > 0:
                    l.append(nums[j])
            output.append(l)
        return output