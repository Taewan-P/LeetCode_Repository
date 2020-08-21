class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        item = self.data.get(key)
        if item:
            self.data[key] += 1
        else:
            self.data[key] = 1 
            
             

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        item = self.data.get(key)
        if not item:
            return None
        elif item == 1:
            self.data.pop(key)
        else:
            self.data[key] -= 1
            
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return "" if not self.data else max(self.data, key=self.data.get)
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return "" if not self.data else min(self.data, key=self.data.get)
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()