class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, curr) :
            if node == len(graph)-1 :
                res.append(curr)
            else :
                for v in graph[node] :
                    dfs(v, curr + [v])
                    
        res = []
        dfs(0, [0])
        return res