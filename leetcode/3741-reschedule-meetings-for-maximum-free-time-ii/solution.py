class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        prev = 0
        stack = []
        for i in range(n):
            stack.append(startTime[i] - prev)
            prev = endTime[i]
        stack.append(eventTime - prev)

        if len(stack) == 1:
            return stack[0]
        
        print(stack)

        max_time = 0
        max_avail_time = 0
        for i in range(1, n + 1):
            curr_time = stack[i - 1] + stack[i]
            meeting_time = endTime[i - 1] - startTime[i - 1]
            if meeting_time <= max_avail_time:
                curr_time += meeting_time
            max_time = max(max_time, curr_time)
            max_avail_time = max(max_avail_time, stack[i - 1])
        
        max_avail_time = 0
        for i in range(n - 1, -1, -1):
            # print(max_avail_time, i)
            curr_time = stack[i + 1] + stack[i]
            meeting_time = endTime[i] - startTime[i]
            if meeting_time <= max_avail_time:
                curr_time += meeting_time
            max_time = max(max_time, curr_time)
            max_avail_time = max(max_avail_time, stack[i + 1])
        
        return max_time
            
        
