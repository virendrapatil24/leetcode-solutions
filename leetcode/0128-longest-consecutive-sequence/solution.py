class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        lg_seq = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            
            curr_seq = 1
            while num + curr_seq in nums_set:
                curr_seq += 1
            lg_seq = max(curr_seq, lg_seq)

        return lg_seq
        
