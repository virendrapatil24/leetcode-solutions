class Solution:
    def numIdenticalPairs(self, num: List[int]) -> int:
        count = 0
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i] == num[j]: count += 1
                    
        return count