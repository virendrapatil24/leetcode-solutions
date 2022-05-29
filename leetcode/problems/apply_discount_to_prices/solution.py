class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        l = sentence.split()
        aplha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",'p','q',"r","s","t","u","v","w","x","y","z","$",""]
        for i in range(len(l)):
            if l[i][0] == "$":
                x = l[i][1:]
                if len(x) == 0: continue
                newl = [i for i in x]
                flag = True
                for j in newl:
                    if j in aplha:
                        flag = False
                        break               
                if flag ==True: l[i] = "$" + "{:.2f}".format(int(x) - (int(x) * discount / 100))
        s = " ".join(l)
        return s