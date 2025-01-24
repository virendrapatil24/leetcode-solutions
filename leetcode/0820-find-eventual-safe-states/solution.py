class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        is_safe = {}
        def dfs(i):
            if i in is_safe:
                return is_safe[i]
            
            is_safe[i] = False
            for neighbour in graph[i]:
                if not dfs(neighbour):
                    return False
            is_safe[i] = True
            return True

        safe = []
        for i in range(len(graph)):
            if dfs(i):
                safe.append(i)
        return safe
        
