class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        new_list = []
        x = nums[0]
        for j in range(len(x)):
            flag = 0
            for i in nums:
                if x[j] in i:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                new_list.append(x[j])
                new_list.sort()
        return new_list;
                
            
            
        