class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i, j = 1, 1
        while i < len(word):
            if word[i] == word[i-1] and j < 9:
                j += 1
            else:
                comp += str(j) + word[i-1]
                j = 1
            i += 1
        comp += str(j) + word[i-1]
        return comp
        



        
