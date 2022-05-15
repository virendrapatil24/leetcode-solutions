class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        i = bottom
        j = 0
        count = 0
        max_count = 0
        special.sort()
        while i < (top+1):
            if j < len(special):
                count = special[j] - i
                max_count= max(max_count,count)
                i = special[j] + 1
                j += 1
            else:
                count = top - i + 1
                max_count= max(max_count,count)
                break
        return max_count
            
        