class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i, t in enumerate(T):
            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append([i, t])
        return res



        