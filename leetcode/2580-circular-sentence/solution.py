class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_list = sentence.split(" ")
        if sentence_list[0][0] != sentence_list[-1][-1]:
            return False
        for i in range(1, len(sentence_list)):
            if sentence_list[i-1][-1] != sentence_list[i][0]:
                return False
        return True
        
        
