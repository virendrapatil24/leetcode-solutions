class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return abs(a * b) // gcd(a, b)

    def gcd_array(self, arr):
        return reduce(gcd, arr)

    def lcm_array(self, arr):
        return reduce(lcm, arr)

    def maxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_array = nums[i:j + 1]
                prod = reduce(lambda x, y: x * y, sub_array)
                lcm = self.lcm_array(sub_array)
                gcd = self.gcd_array(sub_array)
                
                if prod == lcm * gcd:
                    max_len = max(max_len, len(sub_array))
        return max_len
