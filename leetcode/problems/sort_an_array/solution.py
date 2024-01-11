class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.buildHeap(nums, n)
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.maxHeapify(nums, i, 0)
        return nums

    def buildHeap(self, nums, n):
        for i in range((n-2)//2, -1, -1):
            self.maxHeapify(nums, n, i)

    def maxHeapify(self, nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right
        if i != largest:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.maxHeapify(nums, n, largest)
        