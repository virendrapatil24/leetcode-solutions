class Solution:
    def finalValueAfterOperations(self, ops: List[str]) -> int:
        X = 0
        for i in ops:
            if i == "++X" or i == "X++":
                X += 1
            else:
                X -= 1
        return X
            
        