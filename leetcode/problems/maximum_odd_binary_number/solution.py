class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_set_bits = 0
        n = int(s, 2)
        while n:
            n = n & (n - 1)
            count_set_bits += 1
        return ("1" * (count_set_bits - 1)) + ("0" * (len(s) - count_set_bits)) + "1"

        