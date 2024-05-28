class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start, curr_cost, max_len = 0, 0, 0
        for end in range(n):
            curr_cost += abs(ord(s[end]) - ord(t[end]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
        
