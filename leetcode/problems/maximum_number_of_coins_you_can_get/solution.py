class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = int(len(piles)/3)
        return sum(sorted(piles)[n::2])
        