class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            left = s[:i].count("0")
            right = s[i:].count("1")
            if ans < (left + right):
                ans = left + right

        return ans