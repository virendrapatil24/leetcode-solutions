class Solution:
    def criticalConnections(self, n: int, c: List[List[int]]) -> List[List[int]]:
        graph =  [[] for _ in range (n)]
        
        currentRank = 0 
        
        lowestRank = [i for i in range(n)]
        
        visited = [False for _ in range(n)]
        
        for node in c:
            graph[node[0]].append(node[1]) 
            graph[node[1]].append(node[0])
            
        res = []
        
        prevVertex = -1
        currentVertex = 0
        
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        
        return res
    
    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):
        
        visited[currentVertex] = True
        lowestRank[currentVertex] = currentRank
        
        for nextVertex in graph[currentVertex]:
            if nextVertex == prevVertex:
                continue
                
            if not visited[nextVertex]:
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
                
            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
            
            if lowestRank[nextVertex] >= currentRank + 1:
                res.append([currentVertex, nextVertex])
        
        