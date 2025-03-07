class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(temp, open_count, close_count):
            if len(temp) == n * 2:
                res.append(temp)
                return
            
            if open_count < n:
                dfs(temp + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                dfs(temp + ")", open_count, close_count + 1)


        dfs("", 0, 0)
        return res
