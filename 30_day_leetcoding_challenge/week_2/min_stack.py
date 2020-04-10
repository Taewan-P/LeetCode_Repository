class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__min = 0
        self.__topnum = 0
        self.__len = 0
        self.__val = []
        

    def push(self, x: int) -> None:
        self.__val.append(x)
        self.__len = len(self.__val)
        self.__min = min(self.__val)
        

    def pop(self) -> None:
        self.__val.pop()
        self.__len = self.__len - 1
        if self.__len == 0:
            self.__min = None
        else:
            self.__min = min(self.__val)
        

    def top(self) -> int:
        self.__topnum = self.__val[-1]
        return self.__topnum
        

    def getMin(self) -> int:
        return self.__min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
