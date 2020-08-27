class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(l,r,s):
            if l < r:
                return
            
            if r == n:
                result.append(s)
                return
            
            if l < n:
                generate(l+1, r, s + "(")
                
            if r < n:
                generate(l, r+1, s + ")")
                
                
        generate(0,0,"")
        
        return result