class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        directions = [0] * n
        for l, r, sh in shifts:
            if sh == 1:
                directions[l] += 1
                if r + 1 < n: directions[r + 1] -= 1
            else:
                directions[l] -= 1
                if r + 1 < n: directions[r + 1] += 1
        
        s = list(s)
        shift = 0
        for i in range(len(s)):
            shift = (shift + directions[i]) % 26
            if shift < 0:
                shift += 26
            s[i] = chr((ord(s[i]) - ord("a") + shift) % 26 + ord("a"))

        return "".join(s)
        
