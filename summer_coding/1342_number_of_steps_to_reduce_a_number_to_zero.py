class Solution:
    def numberOfSteps (self, num: int) -> int:
        n = 0
        while num != 0:
            if num % 2 == 0:
                # Even
                num = num/2
            else:
                # Odd
                num -= 1
            n += 1
            
        return n