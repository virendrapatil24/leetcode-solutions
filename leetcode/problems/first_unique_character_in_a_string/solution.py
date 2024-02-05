class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_char = {}
        for char in s:
            map_char[char] = map_char.get(char, 0) + 1
        for idx, char in enumerate(s):
            if map_char[char] == 1:
                return idx
        return -1
        