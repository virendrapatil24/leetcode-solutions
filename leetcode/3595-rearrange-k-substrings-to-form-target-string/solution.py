class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        s1 = []
        p1 = []
        size = len(s)//k
        for i in range(k):
            s1.append(s[i*size:size+i*size])
        for i in range(k):
            p1.append(t[i*size:size+i*size])
        return sorted(s1) == sorted(p1)
