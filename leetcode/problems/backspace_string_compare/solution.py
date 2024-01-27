from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        strS, strT = deque(), deque()
        for char in s:
            if char == "#":
                if not strS: continue
                strS.pop()
            else:
                strS.append(char)
        for char in t:
            if char == "#":
                if not strT: continue
                strT.pop()
            else:
                strT.append(char)
        return strS == strT
        