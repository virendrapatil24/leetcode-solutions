class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def digitCount(num):

            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            return digit_sum
            
        sum_map = {}
        for num in nums:
            digit_sum = digitCount(num)
            sum_map[digit_sum] = sum_map.get(digit_sum, []) + [num]
        
        max_sum = -1
        for k, v in sum_map.items():
            if len(v) > 1:
                v.sort()
                max_sum = max(max_sum, sum(v[-2:]))
        
        return max_sum

        
