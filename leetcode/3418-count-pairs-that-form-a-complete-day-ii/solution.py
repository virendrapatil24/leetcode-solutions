class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hashMap = {}
        count = 0
        for hour in hours:
            remainder = hour % 24
            if remainder == 0:
                count += hashMap.get(0, 0)
            else:
                count += hashMap.get(24 - remainder, 0)
            hashMap[remainder] = hashMap.get(remainder, 0) + 1
        return count
