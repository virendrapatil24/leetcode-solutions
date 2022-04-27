class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split(" ")
        while "" in new:
            new.remove("")
        n = len(new[-1])
        return n
        