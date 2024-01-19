class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = (s1+" "+s2).split()
        sMap, res = defaultdict(int), []
        for strg in s:
            sMap[strg] += 1
        for k, v in sMap.items():
            if v == 1:
                res.append(k)
        return res

        