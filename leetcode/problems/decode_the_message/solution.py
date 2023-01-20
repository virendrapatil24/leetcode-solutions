class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_map = {' ': ' '}
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        i = 0

        for char in key:
            if char not in key_map:
                key_map[char] = alpha[i]
                i += 1
                if i == 26:
                    break

        res = ""
        for char in message:
            res += key_map[char]
        
        return res