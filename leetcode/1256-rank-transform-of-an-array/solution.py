class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_map = {}
        sorted_set = sorted(list(set(arr)))
        for i in range(len(sorted_set)):
            rank_map[sorted_set[i]] = i + 1
        for j in range(len(arr)):
            arr[j] = rank_map[arr[j]]
        return arr

        
