class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type": x = 0
        elif ruleKey == "color": x = 1
        elif ruleKey == "name": x = 2   
            
        res = 0
        
        for i in items:
            if i[x] == ruleValue:
                res += 1
        
        return res