class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        flag = False
        for i in sat:
            if i >= 0:
                flag = True
        
        if flag == False : return 0
        
        sat.sort()
        ans = 0
        for i in range(len(sat)):
            res = 0
            a = 1
            for i in range(i, len(sat)):
                res += a * sat[i]
                a += 1
            ans = max(ans, res)
        
        return ans