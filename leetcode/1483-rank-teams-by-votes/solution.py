class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = {}
        m = len(votes[0])
        for vote in votes:
            for i in range(m):
                val = ranks.get(vote[i], [0 for _ in range(m)])
                val[i] += 1
                ranks[vote[i]] = val
        res = sorted(ranks.keys())
        res.sort(key=lambda team: ranks[team], reverse=True)
        print(res)
        return "".join(res)
