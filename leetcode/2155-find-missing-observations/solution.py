class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = (m + n) * mean 
        miss = total_sum - sum(rolls)

        if miss > 6 * n or miss < n: 
            return []
        
        res = [1] * n
        miss -= n

        for i in range(n):
            res[i] += min(5, miss)
            miss -= 5
            if miss <= 0:
                break
        
        return res



        
