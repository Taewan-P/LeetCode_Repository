import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        regex = re.compile(p)
        return bool(regex.fullmatch(s))