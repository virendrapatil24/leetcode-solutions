class Solution:
    def frequencySort(self, s: str) -> str:
        sMap = {}
        for char in s:
            if char in sMap:
                sMap[char] += 1
            else:
                sMap[char] = 1
        newMap = sorted(sMap.items(), key=lambda item:item[1], reverse=True)

        res = ""
        for k, v in newMap:
            res += k * v

        return res 
