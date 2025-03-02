class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == 1:
            hash_map = {} 
            for num in nums:
                hash_map[num] = hash_map.get(num, 0) + 1

            highest = -1
            for k, v in hash_map.items():
                if v == 1:
                    highest = max(highest, k)

            return highest

        if k == len(nums):
            return max(nums)
                
                
        nums_set = set(nums[1:-1])

        first = nums[0]
        last = nums[-1]
        if (first in nums_set and last in nums_set) or first == last:
            return -1

        if first in nums_set:
            return last

        if last in nums_set:
            return first

        return first if first > last else last
        
        
