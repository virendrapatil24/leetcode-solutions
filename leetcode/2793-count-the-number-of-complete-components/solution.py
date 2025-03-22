class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(v, res):
            if v in visited:
                return
            visited.add(v)
            res.append(v)
            for nei in adj.get(v, []):
                dfs(nei, res)
            return res
            
        adj = {}
        for u, v in edges:
            adj[u] = adj.get(u, []) + [v]
            adj[v] = adj.get(v, []) + [u]
        
        count = 0
        visited = set()
        for v in range(n):
            if v in visited:
                continue
            component = dfs(v, [])
            if all(len(adj.get(v2, [])) == len(component) - 1 for v2 in component):
                count += 1
        return count
        
        
