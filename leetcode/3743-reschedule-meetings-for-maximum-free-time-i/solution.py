class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        prev = 0
        stack = []
        for i in range(n):
            stack.append(startTime[i] - prev)
            prev = endTime[i]
        stack.append(eventTime - prev)

        max_time = 0
        k = k + 1
        for i in range(k):
            max_time += stack[i]
        # print(max_time)
        # print(stack)

        curr_time = max_time
        for i in range(k, n + 1):
            curr_time = curr_time - stack[i - k] + stack[i]
            max_time = max(max_time, curr_time)
            

        return max_time
            
        
