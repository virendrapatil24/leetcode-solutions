class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string_sum = ""
        for char in s:
            string_sum += str(ord(char) - ord("a") + 1)
        while k:
            string_sum = str(sum([int(num) for num in string_sum]))
            k -= 1
        return int(string_sum)
        
