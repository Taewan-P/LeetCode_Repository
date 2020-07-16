class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split()
        tmp.reverse()
        return ' '.join(tmp)