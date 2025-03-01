class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        max_min_bound = -inf
        min_max_bound = inf

        for i in range(n):
            curr_min_bound = bounds[i][0] - original[i]
            curr_max_bound = bounds[i][1] - original[i]

            max_min_bound = max(max_min_bound, curr_min_bound)
            min_max_bound = min(min_max_bound, curr_max_bound)

        return max(0, min_max_bound - max_min_bound + 1)

    
        
