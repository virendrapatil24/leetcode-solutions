class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        d = {}
        for i in range(len(searchWord)):
            for word in products:
                if len(word) > i and word[:i+1] == searchWord[:i+1]:
                    if searchWord[:i+1] not in d.keys():
                        d[searchWord[:i+1]] = [word]
                    else:
                        d[searchWord[:i+1]].append(word)
            if searchWord[:i+1] not in d:
                d[searchWord[:i+1]] = []
        res = []
        for key, value in d.items():
            #if len(value) == 0:
                #res.append([])
            if len(value) >= 3:
                res.append(value[:3])
            else:
                res.append(value)
        return res
        
    
                                                                  
                    