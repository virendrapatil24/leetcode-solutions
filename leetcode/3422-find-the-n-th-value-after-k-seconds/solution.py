class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        resLst = [1 for _ in range(n)]
        for i in range(k):
            for j in range(1, n):
                resLst[j] = resLst[j] + resLst[j-1]
        return resLst[-1] % (10**9 + 7)
        
