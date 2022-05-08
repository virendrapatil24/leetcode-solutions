class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3: return ''
        max_n = 0
        num_str = ''
        for i in range (len(num) - 2):
            if int(num[i]) == int(num[i+1]) and int(num[i+1]) == int(num[i+2]):
                num_str = num[i] * 3
      
                if int(num[i]) > max_n:
                    max_n = int(num[i])
                if num_str == '999': return '999'
        
        if num_str == '' : return ''
                
        return str(max_n)*3
        