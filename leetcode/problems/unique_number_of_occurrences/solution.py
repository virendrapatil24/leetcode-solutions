class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        occrSet, count = set(), 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                if count in occrSet:
                    return False
                else:
                    occrSet.add(count)
                    count = 1
            else:
                count += 1
        return count not in occrSet
        