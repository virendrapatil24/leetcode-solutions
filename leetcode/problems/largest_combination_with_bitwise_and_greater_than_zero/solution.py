class Solution:
    def largestCombination(self, c: List[int]) -> int:
        
        l = [0 for i in range(32)]
            
        for i in range(len(c)):
            max_c =31
                
            while(c[i]>0):
                    
                if (c[i] & 1 == 1):
                    
                    l[max_c] += 1
                    
                c[i] = c[i] >> 1
                    
                max_c -= 1
        
        return max(l)
            
            
            
            