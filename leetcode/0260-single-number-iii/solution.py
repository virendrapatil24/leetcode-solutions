class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        right_most_set_bit = xor_result ^ (xor_result & (xor_result - 1))

        num1, num2 = 0, 0
        for num in nums:
            if right_most_set_bit & num != 0:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
        
