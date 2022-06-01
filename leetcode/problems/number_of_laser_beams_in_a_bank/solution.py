class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        i = 0
        j = 1
        while i < (len(bank) - 1) and j < len(bank):
            a = bank[i].count('1')
            b = bank[j].count('1')
            if a == 0:
                i += 1
                j = i + 1
            elif b == 0:
                j += 1
            else:
                res += a * b
                i += 1
                j += 1
        return res
            