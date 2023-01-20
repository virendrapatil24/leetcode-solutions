class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = 'qwertyuiopasdfghjklzxcvbnm'
        for char in alpha:
            if char not in sentence:
                return False
        return True