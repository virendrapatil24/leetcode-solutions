class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hash_map = {}
        for card in hand:
            hash_map[card] = hash_map.get(card, 0) + 1

        sorted_keys = sorted(hash_map.keys())
        for key in sorted_keys:
            if hash_map[key] > 0:
                start_count = hash_map[key]
                for i in range(key, key + groupSize):
                    if hash_map.get(i, 0) < start_count:
                        return False
                    hash_map[i] -= start_count

        return True

        
