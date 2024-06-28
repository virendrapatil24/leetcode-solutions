class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        map_roads = {}
        for s, e in roads:
            map_roads[s] = map_roads.get(s, 0) + 1
            map_roads[e] = map_roads.get(e, 0) + 1
        city_val = [(city, val) for city, val in map_roads.items()]
        city_val.sort(key=lambda x: x[1])
        max_imp = 0
        for i in range(len(city_val) - 1, -1, -1):
            max_imp += n * city_val[i][1]
            n -= 1
        return max_imp

