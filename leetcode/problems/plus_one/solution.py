class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = int("".join(list(map(lambda x: str(x), digits)))) + 1
        return [int(i) for i in str(digits)]
