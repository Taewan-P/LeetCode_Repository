class Solution:
    def maximum69Number (self, num: int) -> int:
        case = [num]
        l = list(str(num))
        for i, n in enumerate(l):
            tmp = list(l)
            if n == "6":
                tmp[i] = "9"
                case.append(int("".join(tmp)))
            else:
                tmp[i] = "6"
                case.append(int("".join(tmp)))
        
        print(case)
        return max(case)