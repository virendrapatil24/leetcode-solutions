class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        countWord1 = [0] * 26
        countWord2 = [0] * 26
        for i in range(len(word1)):
            countWord1[ ord(word1[i]) - ord('a')] += 1
            countWord2[ ord(word2[i]) - ord('a')] += 1
        countWord1.sort()
        countWord2.sort()
        return countWord1 == countWord2 and set(word1) == set(word2)

        