class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        split = len(nums)
        for i in range(len(nums)):
            if nums[i] >= 0: 
                split = i
                break
        neg = nums[:split][::-1]
        pos = nums[split:]
        res = nums
        i, j, k = 0, 0, 0
        print(neg, pos)

        while j < len(neg) and k < len(pos):
            if neg[j] ** 2 < pos[k] ** 2:
                res[i] = neg[j] ** 2
                i += 1
                j += 1
            else:
                res[i] = pos[k] ** 2
                i += 1
                k += 1
        
        while j < len(neg):
            res[i] = neg[j] ** 2
            i += 1
            j += 1
        
        while k < len(pos):
            res[i] = pos[k] ** 2
            i += 1
            k += 1
        
        return res


