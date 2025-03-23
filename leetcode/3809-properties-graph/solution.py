class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:

        def intersect(a, b):
            set_a = set(a)
            visited = set()
            count = 0
            for num in b:
                if num in a and num not in visited:
                    count += 1
                    visited.add(num)
            return count

        adj = defaultdict(list)
        for i in range(len(properties)):
            for j in range(len(properties)):
                # print(intersect(properties[i - 1], properties[i]), k)
                if i != j and intersect(properties[i], properties[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)
        # print(adj)

        def dfs(v):
            if v in visited:
                return
            visited.add(v)
            for nei in adj[v]:
                dfs(nei)
            return

        components = 0
        visited = set()
        for v in range(len(properties)):
            if v in visited:
                continue
            dfs(v)
            components += 1 
        return components
                
        
