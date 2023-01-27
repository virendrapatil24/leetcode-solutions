class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for idx, ops in enumerate(operations):
            if ops == "+":
                res.append(res[-1]+res[-2])
            elif ops == "D":
                res.append(res[-1]*2)
            elif ops == "C":
                res.pop()
            else:
                res.append(int(ops))
        return sum(res)