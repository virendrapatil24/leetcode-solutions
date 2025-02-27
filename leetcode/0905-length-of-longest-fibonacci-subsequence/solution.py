class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_len = 0
        arr_set = set(arr)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                first = arr[i]
                second = arr[j]
                length = 2
                while first + second in arr_set:
                    length += 1
                    temp = first
                    first = second
                    second = temp + second
                max_len = max(length, max_len)
        return max_len if max_len > 2 else 0
