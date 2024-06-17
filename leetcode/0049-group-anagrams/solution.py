class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            hashMap[tuple(sorted(word))] = hashMap.get(tuple(sorted(word)), []) + [word]
        return hashMap.values()

