class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = 0
        for i in range(1, len(intervals)):
            if intervals[res][1] >= intervals[i][0]:
                intervals[res][1] = max(intervals[res][1], intervals[i][1]) 
            else:
                res += 1
                intervals[res] = intervals[i]
        return intervals[:res+1]
        
