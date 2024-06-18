class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        max_matches = 0
        players.sort()
        trainers.sort()
        i = 0
        for player in players:
            while i < len(trainers) and trainers[i] < player:
                i += 1
            if i >= len(trainers):
                break
            max_matches += 1
            i += 1
            
        return max_matches
        
