class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_set = set()
        res = set()
        for num in nums:
            if num in nums_set:
                res.add(num)
            else:
                nums_set.add(num)
        return list(res)
                

        
