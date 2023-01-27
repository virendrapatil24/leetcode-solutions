class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_a = 0
        a = 0
        for i in range(len(gain)):
            if a + gain[i] > max_a:
                a += gain[i]
                max_a = a 
            else:
                a += gain[i] 
        return max_a
