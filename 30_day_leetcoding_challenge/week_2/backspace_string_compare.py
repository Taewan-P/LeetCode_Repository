class Solution:
  def backspaceCompare(self, S: str, T: str) -> bool:
    s_result = self.backspaceConverter(S)
    t_result = self.backspaceConverter(T)

    if (s_result == t_result):
      return True
    else:
      return False

  def backspaceConverter(self, txt: str) -> list:
    a = list(txt)
    result = []
    for i in a:
      if (i == "#"):
        # Backspace
        if (len(result) != 0):
          result.pop(-1)
        else:
          result.append(i)

    return result