class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for idx, scr in enumerate(score):
            heappush(heap, (-scr, idx))

        medal_map = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}

        res = [0] * len(score)

        for rank in range(1, len(score)+1):
            _, idx = heappop(heap)
            res[idx] = medal_map.get(rank, str(rank))

        return res

        