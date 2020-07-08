import re
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        tmp = ""
        result = ""
        
        for i in list(s):
            if i == "[" and stack == []:
                stack.append(i)
                tmp += "!"
            elif i == "[" and stack != []:
                stack.append(i)
                tmp += i
            elif i == "]" and len(stack) == 1:
                stack.pop()
                tmp += "!"
                tmp += "/"
            elif i == "]" and len(stack) != 1:
                stack.pop()
                tmp += i
            else:
                tmp += i
                
        splitted = ' '.join(tmp.split("/")).split()
        # ["2[bc]", "a12bc"]
        
        for e in splitted:
            if "[" in e:
                tmpbool = False
                continuous = True
                t = ""
                num = ""
                tmpstr = ""
                for i in e:
                    if i.isdigit():
                        # If number
                        if not tmpbool:
                            # Never appeared
                            num += i
                            tmpbool = True
                            continuous = True
                        else:
                            # Appeared before
                            if continuous:
                                # Continuous
                                num += i
                            else:
                                tmpstr += i

                    else:
                        # Str
                        if not tmpbool:
                            # if number appeared
                            if continuous:
                                continuous = False
                            t += i
                        else:
                            # number did not appear
                            tmpstr += i
                            continuous = False
                t += int(num) * tmpstr
                result += self.decodeString(t)
            else:
                tmpbool = False
                continuous = True
                num = ""
                tmpstr = ""
                for j in e:
                    if j.isdigit():
                        # If number
                        if not tmpbool:
                            # Never appeared
                            num += j
                            tmpbool = True
                            continuous = True
                        else:
                            # Appeared before
                            if continuous:
                                # Continuous
                                num += j
                            else:
                                tmpstr += j
                    else:
                        # Str
                        if not tmpbool:
                            # if number appeared
                            if continuous:
                                continuous = False
                            result += j
                        else:
                            # number did not appear
                            tmpstr += j
                            continuous = False

                if num == "":
                    result += tmpstr
                else:
                    result += int(num) * tmpstr
                
        return result.replace("!", "")