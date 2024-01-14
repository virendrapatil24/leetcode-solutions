class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        self.buildHeapify(nums, n)
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.maxHeapify(nums, i, 0)

    def buildHeapify(self, nums, n):
        for i in range((n-2)//2, -1, -1):
            self.maxHeapify(nums, n, i)

    def maxHeapify(self, nums, n, i):
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2
        if left < n and nums[largest] < nums[left]:
            largest = left
        if right < n and nums[largest] < nums[right]:
            largest = right
        if i != largest:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.maxHeapify(nums, n, largest)

    

        