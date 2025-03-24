class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def dfs(curr, idx):
            if idx == n:
                res.append(curr[:])
            
            for i in range(idx, n):
                curr_sub_str = s[idx: i + 1]
                if curr_sub_str == curr_sub_str[::-1]:
                    curr.append(curr_sub_str)
                    dfs(curr, i + 1)
                    curr.pop()
        
        dfs([], 0)
        return res
        
