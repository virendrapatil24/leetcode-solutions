class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        nums.sort(key=lambda val: (hash_map[val], -val))
        return nums
        
