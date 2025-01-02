class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        m = len(word) - numFriends + 1
        if numFriends == 1:
            return word
        return max([word[i:i + m] for i in range(len(word))])
        
