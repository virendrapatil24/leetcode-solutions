class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre_req, crs in prerequisites:
            adj[crs].append(pre_req)
        
        def dfs(crs):
            if crs not in pre_req_map:
                pre_req_map[crs] = set()
                for pre_req in adj[crs]:
                    pre_req_map[crs] |= dfs(pre_req)
                pre_req_map[crs].add(crs)
            return pre_req_map[crs]
        
        pre_req_map = {} 
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in pre_req_map[v])
        
        return res
        
