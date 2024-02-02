class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        for j in range(len(str(low)), len(str(high)) + 1):
            i = 0
            while i + j <= 9:
                temp = int(s[i:i+j])
                # print(temp)
                if low <= temp <= high:
                    res.append(temp)
                i += 1
        return res
            



        