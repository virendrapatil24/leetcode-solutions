class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        j = 0
        for i in range(1, len(meetings)):
            if meetings[i][0] <= meetings[j][1]:
                meetings[j][1] = max(meetings[j][1], meetings[i][1])
            else:
                j += 1
                meetings[j] = meetings[i]
        print("meetings", meetings, j)
        available_days = 0
        prev = 0
        for k in range(j + 1):
            curr = meetings[k][0]
            # print(curr, prev, available_days)
            if curr >= days:
                curr = days
                available_days += curr - prev - 1
                prev = meetings[k][1]
                break
            available_days += curr - prev - 1    
            prev = meetings[k][1]
        
        if prev < days:
            available_days += days - prev
        return available_days
