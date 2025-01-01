class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros, max_score = 0, 0
        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            max_score = max(max_score, zeros + ones)
        return max_score
