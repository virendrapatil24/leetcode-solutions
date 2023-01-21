class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0 for i in range(n)]
        def dfs(i):
            if visited[i] == 1:
                return
            
            visited[i] = 1

            for room in rooms[i]:
                dfs(room)

        dfs(0)

        if 0 in visited: return False

        return True
            