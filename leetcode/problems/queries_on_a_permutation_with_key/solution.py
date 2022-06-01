class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1,m+1)]
        res = []
        for i in range(len(queries)):
            a = queries[i]
            b = P.index(a)
            res.append(b)
            P.pop(b)
            P.insert(0, a)
        return res