class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = []
        x = 1
        for i in str(n):
            l.append(int(i))
            x *= int(i)
        return x - sum(l)