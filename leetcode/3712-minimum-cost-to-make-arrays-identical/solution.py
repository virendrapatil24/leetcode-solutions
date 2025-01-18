class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:

        is_same = True
        for i in range(len(arr)):
            if abs(arr[i] - brr[i]) != 0:
                is_same = False

        if is_same:
            return 0

        no_split_cost = adj_cost = sum(abs(a - b) for a, b in zip(arr, brr))
        arr.sort()
        brr.sort()

        adj_cost = sum(abs(a - b) for a, b in zip(arr, brr))

        if len(arr) == 1:
            return adj_cost

        rearg_cost = k

        return min(no_split_cost, (adj_cost + rearg_cost))
