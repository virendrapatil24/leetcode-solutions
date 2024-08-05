class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr_map = {}
        for char in arr:
            arr_map[char] = arr_map.get(char, 0) + 1
        count = 0
        for char in arr:
            if arr_map[char] == 1:
                count += 1
                if count == k:
                    return char
        return ""
