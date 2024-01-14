class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapAgm = {}
        for s in strs:
            if tuple(sorted(s)) in mapAgm.keys():
                mapAgm[tuple(sorted(s))].append(s)
            else:
                mapAgm[tuple(sorted(s))] = [s]
        return mapAgm.values()


        