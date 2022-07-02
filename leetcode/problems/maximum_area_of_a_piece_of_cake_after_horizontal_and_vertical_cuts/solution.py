class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        getMaxSpace = lambda cuts, end: max([cuts[0]] + [end-cuts[-1]] + [cuts[i] - cuts[i-1] for i in range(1, len(cuts))])
        return getMaxSpace(sorted(horizontalCuts), h) * getMaxSpace(sorted(verticalCuts), w) % (10**9+7)        