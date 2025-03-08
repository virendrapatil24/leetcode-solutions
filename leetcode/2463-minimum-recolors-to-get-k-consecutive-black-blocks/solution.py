class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_ops = 0
        for i in range(k):
            if blocks[i] == "W":
                min_ops += 1
        
        curr_min_ops = min_ops
        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                curr_min_ops -= 1
            
            if blocks[i] == "W":
                curr_min_ops += 1

            min_ops = min(curr_min_ops, min_ops)

        return min_ops
            

        
