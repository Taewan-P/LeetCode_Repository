class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp = dict()
        result = []
        length = len(T)
        
        for t in range(30, 101):
            val = ""
            for j in range(length):
                if T[j] > t:
                    val += "1"
                else:
                    val += "0"
            temp[t] = val
                
            
        for i in range(length):
            p = temp[T[i]][i+1:]
            index = p.find("1")
            
            if index >= 0:
                result.append(int(index)+1)
            else:
                result.append(0)
                    
        return result