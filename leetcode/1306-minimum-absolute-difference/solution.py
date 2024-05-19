class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_abs = arr[1] - arr[0]
        for i in range(1, len(arr)):
            curr_min_abs = abs(arr[i] - arr[i-1])

            if curr_min_abs < min_abs:
                min_abs = curr_min_abs
                res.clear()
                res.append([arr[i - 1], arr[i]])
            elif curr_min_abs == min_abs:
                res.append([arr[i - 1], arr[i]])

        return res 
        
