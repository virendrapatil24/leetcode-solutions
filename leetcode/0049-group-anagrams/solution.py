class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_angm = {}
        for strg in strs:
            map_angm[tuple(sorted(strg))] = map_angm.get(tuple(sorted(strg)), []) + [strg]
        return map_angm.values()

