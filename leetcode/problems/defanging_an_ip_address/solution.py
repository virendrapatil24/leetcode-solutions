class Solution:
    def defangIPaddr(self, add: str) -> str:
        ans = ""
        for i in add:
            if i == ".":
                ans = ans + "[" + i + "]"
            else:
                ans = ans + i
        return ans