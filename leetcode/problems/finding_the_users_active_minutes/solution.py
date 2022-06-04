class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = collections.defaultdict(set)
        for a, b in logs:
                d[a].add(b)
        res = [0 for _ in range(k)]
        
        for i in d:
            l = len(d[i])
            res[l-1] += 1
        
        return res
                