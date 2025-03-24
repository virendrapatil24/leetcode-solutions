class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        n = len(digits)

        def dfs(strg, idx):
            if strg and len(strg) == n:
                res.append(strg)
                return

            if idx >= n:
                return

            for i in range(idx, n):
                for char in num_char_map[digits[i]]:
                    dfs(strg + char, i + 1)
    
        dfs("", 0)
        return res
        
