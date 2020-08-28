# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = self.flatten(nestedList)
        self.length = len(self.flattened)
        self.index = 0 if self.length >= 0 else -1
        
                
    def flatten(self, nested: [NestedInteger]) -> list:
        result = []
        
        def generate(NIL):
            for NI in NIL:
                if NI.isInteger():
                    result.append(NI.getInteger())
                else:
                    generate(NI.getList())
        
        generate(nested)
        
        return result
            
    
    
    def next(self) -> int:
        self.index += 1
        return self.flattened[self.index - 1]
        
    
    def hasNext(self) -> bool:
        return True if self.index < self.length else False
            
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())