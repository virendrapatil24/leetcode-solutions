class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        gp, pp, mp, res = 0, 0, 0, 0
        for i in range(len(garbage)):
            if garbage[i].count('G') > 0:
                res += garbage[i].count('G') + sum(travel[gp:i])
                gp = i
            if garbage[i].count('P') > 0:
                res += garbage[i].count('P') + sum(travel[pp:i])
                pp = i
            if garbage[i].count('M') > 0:
                res += garbage[i].count('M') + sum(travel[mp:i])
                mp = i
        return res