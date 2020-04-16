class Solution:
  def stringShift(self, s: str, shift: List[List[int]]) -> str:
    left = 0
    right = 0
    for i in shift:
      if (i[0] == 1):
        right += i[1]
      else:
        left += i[1]

    n = left-right
    if (abs(n) > len(s)):
      n = n % len(s) 
    return s[n:] + s[:n]