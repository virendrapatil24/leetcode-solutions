class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        cols, rows, k = len(grid[0]), len(grid), len(queries)
        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()
        ans = [0] * k
        min_heap = [(grid[0][0], 0, 0)]
        points = 0
        visited = set([(0, 0)])

        for limit, idx in q:
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heappop(min_heap)
                points += 1
                neighbours = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
                for nr, nc in neighbours:
                    if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            ans[idx] = points
        return ans
        
