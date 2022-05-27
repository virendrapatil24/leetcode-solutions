class Solution:
    def maximumWealth(self, acc: List[List[int]]) -> int:
        rich = 0
        for i in acc:
            rich = max(sum(i), rich)
        return rich
        