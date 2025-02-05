class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff1 = 0
        diff2 = 0
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1

                if diff > 2:
                    return False
                elif diff == 1:
                    diff1 = i
                else:
                    diff2 = i

        return s1[diff1] == s2[diff2] and s1[diff2] == s2[diff1]

        
