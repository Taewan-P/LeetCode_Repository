class Solution:
    def isHappy(self, n: int) -> bool:
      ans = 0
      history = []
      while True:
        tmp = list(str(n))
        numsum = sum([int(i)**2 for i in tmp])
        if (numsum in history):
          return False
        history.append(numsum)

        if (numsum == 1):
          return True
        else:
          n = numsum