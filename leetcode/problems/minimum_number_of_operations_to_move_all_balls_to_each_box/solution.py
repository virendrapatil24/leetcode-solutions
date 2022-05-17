class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ans = []
    
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if j == i: continue
                if boxes[j] == '0': continue
                else: 
                    count += abs(j-i)
                    
            ans.append(count)
        return ans