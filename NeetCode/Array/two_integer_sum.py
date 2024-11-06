from typing import List

class Solution:
  def two_int_sum(self, nums: List[int], target: int) -> List[int]:

    result = dict() # val -> index

    for i, num in enumerate(nums):

      diff = target - num
      if diff in result:
        return [result[diff], i]  
      result[i] = num
  
if __name__ == "__main__":
  s, t = input().split(" ")

  sol = Solution()

  print(sol.two_int_sum(s, t))