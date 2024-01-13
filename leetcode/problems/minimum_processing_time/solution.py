class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        res, i = 0, 0
        while i < len(tasks):
            maxTime = max(tasks[i:i+4]) + processorTime[i//4]
            if maxTime > res:
                res = maxTime
            i += 4
        return res      