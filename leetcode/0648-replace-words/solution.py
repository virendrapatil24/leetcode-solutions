class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence_lst = sentence.split()
        root_set = set(dictionary)
        res = []
        for word in sentence_lst:
            for i in range(len(word)):
                prefix = word[:i]
                if prefix in root_set:
                    res.append(prefix)
                    break
            else:
                res.append(word)
        return " ".join(res)
        
