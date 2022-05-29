class Solution:
    def groupThePeople(self, grp: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(grp)):
            if grp[i] not in d.keys():
                d[grp[i]] = [i]
            else:
                #pass
                d[grp[i]].append(i)
        res = []
        for a,b in d.items():
            if a == len(b):
                res.append(b)
            else:
                for i in range(len(b)//a):
                    res.append(b[i*a:(i*a)+a])
        return res
                