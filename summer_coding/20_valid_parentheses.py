class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s == "":
            return True
        for i in s:
            if (i == "(" or i == "[" or i == "{"):
                stack.append(i)
            elif (i == ")" or i == "]" or i == "}"):
                if stack:
                    if stack[-1] == "(" and i == ")":
                        stack.pop()
                    elif stack[-1] == "[" and i == "]":
                        stack.pop()
                    elif stack[-1] == "{" and i == "}":
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    return False
                
        if stack:
            return False
        else:
            return True