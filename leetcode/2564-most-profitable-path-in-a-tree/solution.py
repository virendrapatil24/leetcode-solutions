class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        graph = {}
        for u, v in edges:
            graph[u] = graph.get(u, []) + [v]
            graph[v] = graph.get(v, []) + [u]
        
        bob_path_time_map = {}
        def dfs(src, prev, time):
            if src == 0:
                bob_path_time_map[src] = time
                return True
            
            for nei in graph[src]:
                if nei == prev:
                    continue
                if dfs(nei, src, time + 1):
                    bob_path_time_map[src] = time
                    return True
            return False
        dfs(bob, -1, 0)

        q = deque([(0, 0, -1, amount[0])])
        res = -inf
        while q:
            node, time, parent, profit = q.popleft()
            for nei in graph[node]:
                if nei == parent:
                    continue
                nei_profit = amount[nei]
                if nei in bob_path_time_map:
                    if time + 1 > bob_path_time_map[nei]:
                        nei_profit = 0
                    if time + 1 == bob_path_time_map[nei]:
                        nei_profit //= 2
                q.append((nei, time + 1, node, profit + nei_profit))
                if len(graph[nei]) == 1:
                    res = max(res, profit + nei_profit)

        return res
