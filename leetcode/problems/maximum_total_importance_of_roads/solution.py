class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        l = []
        for i in range(len(roads)):
            for j in range(2):
                l.append(roads[i][j])
        
        d = {}
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]] = 1
            else:
                d[l[i]] += 1

        x = [i for i in d.values()]
        x.sort()
        res = 0
        v = len(x) - 1
        w = n - 1
        while v >= 0:
            res += x[v] * (w + 1)
            w -= 1
            v -= 1
        return res