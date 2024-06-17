class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        hashMap = set()
        num = 0
        while num * num <= c:
            hashMap.add(c - num * num)
            if num * num in hashMap:
                return True
            num += 1
        return False
        
