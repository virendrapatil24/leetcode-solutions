class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res = num1 

        target_bits = self.count_ones(num2)
        curr_bits = self.count_ones(num1)

        curr_idx = 0
        while curr_bits < target_bits:
            if not self.is_set(res, curr_idx):
                res = self.set_bit(res, curr_idx)
                curr_bits += 1
            curr_idx += 1

        while curr_bits > target_bits:
            if self.is_set(res, curr_idx):
                res = self.unset_bit(res, curr_idx)
                curr_bits -= 1
            curr_idx += 1

        return res
    
    def count_ones(self, num):
        count = 0
        while num > 0:
            num &= (num - 1)
            count += 1
        return count

    def is_set(self, num, bit):
        return num & (1 << bit) != 0

    def set_bit(self, num, bit):
        return num | (1 << bit)
    
    def unset_bit(self, num, bit):
        return num & ~(1 << bit)
