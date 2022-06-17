class Solution:
    def sumOddLengthSubarrays(self, A: List[int]) -> int:
        return sum(sum(A[i:i + l]) for l in range(1, 100, 2) for i in range(len(A) - l + 1))
            
