class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapAgm = {}
        for s in strs:
            mapAgm[tuple(sorted(s))] = mapAgm.get(tuple(sorted(s)), []) +[s]
        return mapAgm.values()


        