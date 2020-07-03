import re
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        l = len(word)
        self.data[l] = self.data.get(l, []) + [word]
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        l = len(word)
        if "." in word:
            # Regex
            w = self.data.get(l, [])
            regex = re.compile(word)
            for i in w:
                if bool(regex.fullmatch(i)):
                    return True
        else:
            if word in self.data.get(l,[]):
                return True
            else:
                return False
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)