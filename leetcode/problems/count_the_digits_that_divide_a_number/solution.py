class Solution:
    def countDigits(self, num: int) -> int:
        return len([digit for digit in str(num) if num % int(digit) == 0])