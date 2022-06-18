class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        d = {}
        
        for edge in edges:
            if edge[0] not in d:
                d[edge[0]] = [edge[1]]
            else:
                d[edge[0]].append(edge[1])
                
            if edge[1] not in d:
                d[edge[1]] = [edge[0]]
            else:
                d[edge[1]].append(edge[0])
        
        stack = [source]
        
        while len(stack) > 0:
            
            curr = stack.pop()
            
            if curr == destination: return True
            
            if curr in d.keys() and curr not in visited:
                visited.add(curr)
                for neighbour in d[curr]:
                    stack.append(neighbour)
                    
        return False
        
        