class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums_set = set(nums)

        def dfs(strg, n):
            if len(strg) == n:
                return strg

            for i in ["0", "1"]:
                strg += i
                ans = dfs(strg, n)
                if ans and ans not in nums_set:
                    return ans
                strg = strg[:-1]
        return dfs("", n)

        
