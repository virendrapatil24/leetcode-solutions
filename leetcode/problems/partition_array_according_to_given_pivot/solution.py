class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #res = []
        start = []
        mid = []
        end = []
        for i in nums:
            if i < pivot:
                start.append(i)
            elif i > pivot:
                end.append(i)
            else: 
                mid.append(i)
        return start + mid + end