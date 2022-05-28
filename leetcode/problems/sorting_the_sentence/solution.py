class Solution:
    def sortSentence(self, s: str) -> str:
        l = [i for i in s.split()]
        l.sort(key = lambda x: x[-1])
        
        return " ".join(i[:-1] for i in l)