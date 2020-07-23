class Solution:
    def frequencySort(self, s: str) -> str:
        occ = dict()
        result = ""
        
        for i in s:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1
                
        str_list = list(occ.items())
        
        for i in range(len(occ.keys())):
            max_str = ""
            max_count = 0
            for s,n in str_list:
                if n > max_count:
                    max_count = n
                    max_str = s
            
            result += max_str*max_count
            str_list.remove((max_str, max_count))
                
        return result