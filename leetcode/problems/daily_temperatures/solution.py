class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0] * len(temp)
        stack = []
        for i, t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
                #return cur, i, ans
            stack.append(i)

        return ans
            