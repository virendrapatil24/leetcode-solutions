class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def track(l = [], left = 0, right =0):
            if len(l) == 2 * n:
                output.append("".join(l))
                return
            if left < n:
                l.append("(")
                track(l, left + 1, right)
                l.pop()
            if right < left:
                l.append(")")
                track(l, left, right + 1)
                l.pop()
        track()
        return output