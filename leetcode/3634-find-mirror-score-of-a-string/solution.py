class Solution:
    def calculateScore(self, s: str) -> int:
        mirror = {chr(i): chr(219 - i) for i in range(97, 123)}

        n = len(s)
        score = 0
        stack = [[] for _ in range(27)]

        for i in range(n):
            mirror_char = mirror[s[i]]
            lst = stack[ord(mirror_char) - ord("a")]
            if (len(lst) > 0):
                j = stack[ord(mirror_char) - ord("a")].pop()
                score += i - j
            else:
                stack[ord(s[i]) - ord("a")].append(i)
        return score
                
        
