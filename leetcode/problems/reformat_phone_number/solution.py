class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = [n for n in number if n.isdigit()]
        res, i = [], 0
        for i in range(0, len(nums)-1, 3):
            res.append(''.join(nums[i:i+3]))

        if len(nums) - 4 == i:
            last = res[-1]
            res[-1] = last[:2]
            res.append(last[2] + nums[-1])
        
        return '-'.join(res)
        