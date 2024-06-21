class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_customers = 0
        for i in range(len(customers)):
            if grumpy[i]:
                continue
            max_customers += customers[i]
            customers[i] = 0
        curr_max = 0
        for i in range(minutes):
            curr_max += customers[i]
        maximum = max(curr_max, 0)
        for i in range(minutes, len(customers)):
            curr_max += customers[i] - customers[i-minutes]
            maximum = max(curr_max, maximum)
        return maximum + max_customers
