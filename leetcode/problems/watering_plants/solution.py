class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        curr_capacity = capacity
        for i, plant in enumerate(plants):
            if curr_capacity < plant:
                res += 2*i + 1
                curr_capacity = capacity - plant
            else:
                res += 1
                curr_capacity -= plant
        return res