class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = 0
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    arr1[j], arr1[k] = arr1[k], arr1[j]
                    k += 1
        arr1[k:] = sorted(arr1[k:])
        return arr1
