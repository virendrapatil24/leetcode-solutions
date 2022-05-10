class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        return [val for val in itertools.combinations([i for i in range(1,10)], k) if sum(val) == n]