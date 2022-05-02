class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_letter = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        lend = len(digits)
        ans = []
        
        if digits == '': return []
        
        def out_ans(pos: int, st: str):
            if pos ==  lend: ans.append(st) 
            else:
                letters = phone_letter[digits[pos]]
                for letter in letters:
                    out_ans(pos+1,st+letter)
        
        out_ans(0,"")
        return ans