class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        x = set(target)
        count = 101
        #l = []
        for i in x:
            #return s.count(i), target.count(i), i
            if i not in s: return 0
            if s.count(i) >= target.count(i):
                #l.append(target.count(i))
                count = min(count, s.count(i)//target.count(i))
            else:
                return 0
        return count
        