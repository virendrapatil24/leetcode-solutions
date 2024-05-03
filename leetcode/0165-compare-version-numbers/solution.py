class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1_lst, ver2_lst = version1.split("."), version2.split(".")
        m, n = len(ver1_lst), len(ver2_lst)
        i, j = 0, 0
        while i < m and j < n:
            if int(ver1_lst[i]) < int(ver2_lst[j]):
                return -1
            elif int(ver1_lst[i]) > int(ver2_lst[j]):
                return 1
            else:
                i += 1
                j += 1
        
        while i < m:
            if int(ver1_lst[i]) > 0:
                return 1
            else:
                i += 1
        
        while j < n:
            if int(ver2_lst[j]) > 0:
                return -1
            else:
                j += 1
        
        return 0
            

        
