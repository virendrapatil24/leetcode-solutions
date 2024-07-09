class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = 0
        available_at = 0
        for arr, time in customers:
            available_at = max(available_at, arr) + time
            wait_time += available_at - arr
            
        return wait_time / len(customers)
            
                
