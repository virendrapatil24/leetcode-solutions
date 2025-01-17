class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool: 
        start = 0
        for bi in range(len(derived) - 1):
            start ^= derived[bi]
        return start ^ derived[-1] == 0

        
